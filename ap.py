{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "80ceac50-c366-4e57-a104-778d217ab22e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from fastapi import FastAPI, HTTPException\n",
    "from pydantic import BaseModel\n",
    "from typing import List, Dict, Any\n",
    "\n",
    "app = FastAPI()\n",
    "\n",
    "class RecommendationRequest(BaseModel):\n",
    "    student_id: str\n",
    "    student_request: str\n",
    "\n",
    "class RecommendationResponse(BaseModel):\n",
    "    courses: List[Dict[str, Any]]\n",
    "    explanation: str\n",
    "\n",
    "@app.post(\"/recommendation/\", response_model=RecommendationResponse)\n",
    "def get_recommendation(request: RecommendationRequest):\n",
    "    # Fix the missing parenthesis\n",
    "    student = next((s for s in all_students if s.student_id == request.student_id), None)\n",
    "    \n",
    "    if not student:\n",
    "        raise HTTPException(status_code=404, detail=\"Student not found\")\n",
    "    \n",
    "    # Call the function that generates recommendations\n",
    "    try:\n",
    "        recommendations = get_recommendations(student, request.student_request)\n",
    "    except ValueError as e:\n",
    "        raise HTTPException(status_code=500, detail=str(e))\n",
    "    \n",
    "    return recommendations\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "33eb56ea-38a0-4580-877c-03a359ab6cc3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
