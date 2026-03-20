# Master Ji AI Tutor: Your Adaptive Programming Tutor!
An intelligent tutoring platform designed to guide students through coding with hints, adaptive feedback, and real time collaboration. MasterJi AI is designed to act like a real programming tutor. Instead of returning full solutions, it analyzes code submitted by the student, detects errors, and provides hints to improve debugging and confidence.


## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [User Roles](#user-roles)
- [Branch Workflow](#branch-workflow)


# Overview
MasterJi AI is an adaptive coding tutor built to function like a real programming teacher instead of a solution generator.

Instead of returning complete answers, MasterJi AI analyzes student submitted code, detects logical and syntactic errors, identifies misconceptions, and delivers structured hints that guide students toward their own solutions.

The platform combines AI powered feedback, gamified progression, real time collaboration, and role based access for teachers, parents, and administrators to create a complete learning ecosystem.

# Features
Adaptive Feedback Engine
- Real time code analysis
- Syntax and logical error detection
- Misconception recognition
- Step by step guided hints

Gamified Mastery System
- XP points and level progression
- Skill trees by concept
- Achievement badges
- Optional AI mascot for engagement

AI Teacher Avatar
- Interactive AI generated tutor
- Customizable personality modes
- Encourages reflection and explanation

# User Roles
Admin View
- For platform oversight and testing.
- Access to testing panel
- Analytics

Teacher View
- To support instruction and student growth
- Access curriculum and assignments
- Create coding exercises
- Leave feedback
- View mastery analytics and progress trends

Parent View
- For transparency and engagement
- View student grades
- Access teacher comments
- Monitor performance
- Receive milestone updates

Student View

Dashboard
- Current progress overview
- Visual progress bar
- XP points and level tracking
- Skill mastery map
- Upcoming assignments
- Grade summaries

Interactive Learning
- AI generated teacher avatar
- Hints instead of full answers

# Branch Workflow
To keep team work predictable, use the branches this way:

- `frontend`: active UI branch for the website interface and client-side work.
- `backend`: backend endpoints, database work, and Django server logic.
- `RAG`: retrieval, textbook parsing, topic extraction, and lesson generation experiments.
- `API-integration`: external API wiring and service integration work.
- `dev`: shared integration branch when features from the team are ready to test together.
- `main`: stable branch for the cleanest merged version of the project.

Current recommendation:

- Build day-to-day UI work on `frontend`.
- Merge feature work into `dev` for team testing.
- Merge `dev` into `main` only when the combined app is stable.
- Avoid committing new feature work directly to `main`.

Suggested branch naming for personal work:

- `frontend/<name>-<task>`
- `backend/<name>-<task>`
- `rag/<name>-<task>`
- `api/<name>-<task>`
