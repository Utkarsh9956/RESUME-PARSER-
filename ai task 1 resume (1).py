#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import dependancies
import nltk


# In[2]:


#calculating score of candidate on basis of skills
def calculate_score(job_requirements, candidate_skills):
    # Calculate the number of matches between job requirements and candidate skills
    match_count = sum(1 for word in job_requirements if word in candidate_skills)
    return match_count


# In[3]:


#finding the best candidate
def find_best_candidate(job_requirements, candidate_profiles):
    best_candidate = None
    best_score = 0

    for candidate in candidate_profiles:
        candidate_skills = candidate['skills']
        candidate_experience = candidate['experience']
        communication_skills = candidate['communication_skills']
        
        score = calculate_score(job_requirements, candidate_skills)
        
        # Adjust score based on experience
        score += candidate_experience
        
        # Adjust score based on communication skills
        if communication_skills == 'excellent':
            score += 2
        elif communication_skills == 'good':
            score += 1
        
        # Check if the current candidate has a higher score than the previous best candidate
        if score > best_score:
            best_candidate = candidate
            best_score = score

    return best_candidate


# In[4]:


#printing best candidate for the job

def print_candidate(candidate):
    if candidate:
        print("Best candidate for the job:")
        print(f"Name: {candidate['name']}")
        print(f"Skills: {', '.join(candidate['skills'])}")
        print(f"Experience: {candidate['experience']} years")
        print(f"Communication Skills: {candidate['communication_skills']}")
    else:
        print("No suitable candidates found.")


# In[5]:


#taking requirements input for the job
def get_job_requirements():
    job_requirements = []
    while True:
        requirement = input("Enter a job requirement (or 'done' to finish): ")
        if requirement.lower() == 'done':
            break
        job_requirements.append(requirement.lower())
    return job_requirements


# In[6]:


def main():
    # Get job requirements from the user
    print("Enter the job requirements:")
    job_requirements = get_job_requirements()

    # Define candidate profiles
    candidate_profiles = [
        {
            'name': 'MITANSHI',
            'skills': ['python', 'data analysis', 'problem-solving'],
            'experience': 7,
            'communication_skills': 'excellent'
        },
        {
            'name': 'UDAY',
            'skills': ['python', 'machine learning', 'data visualization'],
            'experience': 5,
            'communication_skills': 'good'
        },
        {
            'name': 'VRUNDA',
            'skills': ['python', 'machine learning', 'communication skills'],
            'experience': 2,
            'communication_skills': 'excellent'
        },
        {
            'name': 'MAHI',
            'skills': ['python', 'deep learning', 'communication skills'],
            'experience': 4,
            'communication_skills': 'excellent'
        },
        {
            'name': 'MEDHA',
            'skills': ['python', 'data engineering', 'communication skills'],
            'experience': 6,
            'communication_skills': 'good'
        }
    ]

    # Find the best candidate
    best_candidate = find_best_candidate(job_requirements, candidate_profiles)

    # Output the best candidate
    print_candidate(best_candidate)


# In[10]:


if __name__ == "__main__":
    main()


# In[ ]:




