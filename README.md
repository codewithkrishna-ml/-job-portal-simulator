# Recruitment & Job Portal System 💼🚀

A comprehensive, role-based backend administration engine built in Python using core **Object-Oriented Programming (OOP)** principles. This application models a modern job search marketplace and Applicant Tracking System (ATS), seamlessly routing validation paths between Recruiters (job posting & candidate screening) and Job Seekers (profile building & application logs).

---

## 🌟 About the Developer

*   **Age/Class:** 16 Years Old (Class 10th) 🎯
*   **Future Goal:** B.Tech in Artificial Intelligence and Machine Learning (AI-ML) -> **Aspiring ML Engineer at Google / Microsoft** 🤖⚡
*   **Milestone:** Successfully completed the **100 Days of Code** challenge!
*   **Current Focus:** Mastering Data Structures & Algorithms (DSA) and building data science workflows with **NumPy** and **Pandas**.

---

## ✨ Key Features

*   **Dual Portal Interfaces:** Implements segregated logical flows mapped uniquely for `Candidate` profiles and `Recruiter` dashboard workspaces.
*   **Dynamic Job Registry:** Allows recruiters to post new opening descriptions including Title, Department, Salary metrics, and explicit required skill tags.
*   **Interactive Application Engine:** Job seekers can browse active marketplace openings, update their skill sets, and apply directly to matching tracks.
*   **Automated Skill Match Filter:** Features built-in logic that cross-references a candidate's profile tags against job requirements to flag application eligibilities before submission.
*   **Stateful Hiring Workflows:** Enables recruiters to pull up applicant lists for their specific job postings and toggle review statuses (`Applied` / `Shortlisted` / `Rejected`).

---

## 🛠️ OOP Concepts & Architecture Demonstrated

This enterprise prototype leverages decoupling models to ensure smooth system communication and clean separation of privileges:
*   **Inheritance Hierarchy:** Structures specialized classes `Candidate` and `Recruiter` cleanly underneath a central `User` super-class to reuse core authentication and contact fields.
*   **Relational Aggregation (Composition):** The master orchestration controller class manages multi-tier runtime references—nesting collections of active users and job postings within structural system dictionaries mapping state alterations smoothly.
*   **Objects Cross-Referencing:** Tracks operational bounds by cross-mapping references, where individual `JobApplication` nodes securely capture structural pointers to specific `Job` blueprints and unique `Candidate` objects simultaneously.

---

## 🚀 How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone https://github.com
    ```
2.  **Navigate to the project folder:**
    ```bash
    cd recruitment-job-portal-oop
    ```
3.  **Run the interactive terminal matrix portal:**
    ```bash
    python main.py
    ```

---

## 📝 Prerequisites
*   **Python 3.x** installed on your machine.
*   Runs completely on pure Python core architectures without needing external third-party library installations.
