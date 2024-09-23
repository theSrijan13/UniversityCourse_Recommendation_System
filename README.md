# LLM-Based Course Recommender System

This project is a FastAPI-based API for recommending university courses to students for the next semester. It evaluates student course history, major requirements, and other relevant factors to suggest the best courses while avoiding scheduling conflicts and ensuring prerequisites are met.

## Features

- **Course Recommendation**: Recommends the next semester's course load based on student history, major, and preferences.
- **Schedule Conflict Check**: Ensures no conflicts with course time blocks.
- **Prerequisite Validation**: Verifies that students have completed necessary prerequisites.
- **FastAPI Interface**: Provides an easy-to-use API for interaction.
- **Docker Containerization**: Can be containerized for easy deployment across environments.

## Prerequisites

Ensure you have the following installed:

- [Python 3.10+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/products/docker-desktop) (if running via Docker)
- [FastAPI](https://fastapi.tiangolo.com/)

## Setup

### 1. Clone the Repository

git clone https://github.com/your-username/course-recommender.git
cd course-recommender


### Explanation:
- **Project Overview**: Brief explanation of what the project does.
- **Features**: Highlight the core features of the recommender.
- **Setup**: Steps to clone, install dependencies, and run the app locally.
- **Docker Instructions**: Steps to build and run the app in Docker.
- **API Documentation**: Example request and response for the course recommendation endpoint.
- **Project Structure**: Overview of key files in the project.
- **Future Improvements**: Potential improvements for future development.
- **License**: License information.

### Future Improvements
Enhance the recommendation logic based on student preferences.
Add a scoring system to better rank courses.
Improve the evaluation metrics and add more test cases.
Deploy the API on a cloud service like AWS or Google Cloud.

Replace the placeholder URLs (e.g., `https://github.com/thesrijan13/course-recommender.git`) with your actual GitHub repository link.

