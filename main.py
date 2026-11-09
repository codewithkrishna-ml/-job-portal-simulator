#PROJECT-Recruitment & Job Portal System
class JobPosting:
    def __init__(self, job_id, title, department, status):
        self.job_id = int(job_id)
        self.title = title
        self.department = department
        self.status = status
        self.application_list = []

    def __str__(self):
        return f"Job ID: {self.job_id} | Title: {self.title} | Department: {self.department} | Status: {self.status}"

class RecruitmentManager:
    def __init__(self):
        self.job_db = {}
        self.id_counter = 101

    def create_job(self, title, department):
        if title == "" or department == "":
            print("Error: Field cannot be blank")
            return False

        current_id = self.id_counter
        new_job = JobPosting(current_id, title, department, "Open")

        self.job_db[current_id] = new_job
        self.id_counter += 1

        print(f"Job created successfully with ID: {current_id}")
        return True

    def apply_for_job(self, job_id, applicant_name, experience_years):
        if job_id not in self.job_db:
            print("Error: This job posting does not exist")
            return False

        job = self.job_db[job_id]

        if job.status == "Closed":
            print("Error: This job posting has been closed")
            return False

        if experience_years < 1:
            print(f"Application rejected for {applicant_name}. Minimum 1 year of experience required.")
            return False

        application_entry = f"Name: {applicant_name} (Exp: {experience_years} years)"
        job.application_list.append(application_entry)
        print(f"Yes! Application successfully submitted for Mr. {applicant_name}.")
        return True

    def view_all_jobs(self):
        if len(self.job_db) == 0:
            print("No job openings available currently.")
            return

        print("\n----------------------------- AVAILABLE JOB POSTING ---------------------------------------")
        for j_id in self.job_db:
            print(self.job_db[j_id])
        print("---------------------------------------------------------------------------------------------")

    def view_job_application(self, job_id):
        if job_id not in self.job_db:
            print("Error: Job ID not found")
            return 

        job = self.job_db[job_id]
        print(f"\n-------- Application for Job ID {job_id} ({job.title}) -----------")
        if len(job.application_list) == 0:
            print("No applicants have applied for this job yet")
            return

        for app in job.application_list:
            print(f"-> {app}")

    def close_job(self, job_id):
        if job_id not in self.job_db:
            print("Error: Job ID not found")
            return False

        job = self.job_db[job_id]
        job.status = "Closed"
        print(f"Job ID {job_id} has been successfully closed for new applications")
        return True

    def export_data_csv(self):
        if len(self.job_db) == 0:
            print("No recruiment records found to export")
            return False

        try:
            file = open("recruiment_ledger.csv", mode="w")
            file.write("JobID,JobTitle,Department,Status,TotalApplicants\n")
            for j_id in self.job_db:
                job = self.job_db[j_id]
                file.write(f"{job.job_id},{job.title},{job.department},{job.status},{len(job.application_list)}\n")
            file.close()
            print("Recruitment log successfully exported to 'recruitment_ledger.csv'")
            return True
        except:
            print("Error: writing data matrix to csv storage")
            return False

manager = RecruitmentManager()

while True:
    print("\n---------------------- RECRUITMENT / JOB PORTAL MENU ----------------------------")
    print("1. Create New Job Opening")
    print("2. View All Open Jobs")
    print("3. Apply for a Job (Applicant Entry)")
    print("4. View Applications for a Specific Job")
    print("5. Close a Job Posting")
    print("6. Export Recruitment Data to CSV")
    print("7. Exit")

    choice = input("Select an option (1-7):").strip()

    if choice == "1":
        t_title = input("Enter Job Title:").strip()
        d_dept = input("Enter Department:").strip()
        manager.create_job(t_title, d_dept)

    elif choice == "2":
        manager.view_all_jobs()

    elif choice == "3":
        try:
            j_id = int(input("Enter target Job ID to apply: ").strip())
            name = input("Enter Applicant Full Name: ").strip()
            exp = int(input("Enter Years of Experience: ").strip())
            manager.apply_for_job(j_id, name, exp)
        except ValueError:
            print("Error: Job ID and Experience must be numerical values.")

    elif choice == "4":
        try:
            j_id = int(input("Enter job ID view applicants: ").strip())
            manager.view_job_application(j_id)
        except ValueError:
            print("Error: Job ID must be a vailed number")

    elif choice == "5":
        try:
            j_id = int(input("Enter job ID to close: ").strip())
            manager.close_job(j_id)
        except ValueError:
            print("Error: job must be a vailed number")

    elif choice == "6":
        manager.export_data_csv()

    elif choice == "7":
        print("Safely shutting down recruitment engine portals. Goodbye!")
        break
    else:
        print("Invailed opreational choice! please provide an entry index between 1 and 7")
