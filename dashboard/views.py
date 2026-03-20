# Load JSON request bodies sent from the browser.
import json
# Run submitted Python code in a separate process.
import subprocess
# Access the same Python executable Django is running with.
import sys

# Return JSON responses to frontend requests.
from django.http import JsonResponse
# Render HTML templates into browser responses.
from django.shortcuts import render
# Skip CSRF checks for the local code-run endpoint.
from django.views.decorators.csrf import csrf_exempt
# Limit an endpoint so it only accepts POST requests.
from django.views.decorators.http import require_POST


# Render the main tutor page.
def home(request):
    return render(request, "dashboard/dashboard.html")


# Allow the frontend to send code and get execution results back.
@csrf_exempt
@require_POST
def run_code(request):
    # Try to parse the incoming JSON payload from the browser.
    try:
        payload = json.loads(request.body or "{}")
    # Return a clear error if the request body is not valid JSON.
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON payload."}, status=400)

    # Read the submitted code from the payload.
    code = payload.get("code", "")
    # Reject any request where code is not a normal text string.
    if not isinstance(code, str):
        return JsonResponse({"error": "Code must be a string."}, status=400)

    # Return early if the user tries to run an empty editor.
    if not code.strip():
        return JsonResponse({"stdout": "", "stderr": "No code to run.", "timed_out": False})

    # Run the code in a child process and capture its output safely.
    try:
        result = subprocess.run(
            # Use the current Python interpreter and pass the code with -c.
            [sys.executable, "-c", code],
            # Capture anything printed to stdout and stderr.
            capture_output=True,
            # Decode the output as text instead of raw bytes.
            text=True,
            # Stop long-running programs after five seconds.
            timeout=5,
        )
        # Send the captured output back to the page as JSON.
        return JsonResponse(
            {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "timed_out": False,
            }
        )
    # Return a timeout response if the student code runs too long.
    except subprocess.TimeoutExpired:
        return JsonResponse(
            {
                "stdout": "",
                "stderr": "Execution timed out after 5 seconds.",
                "timed_out": True,
            }
        )
