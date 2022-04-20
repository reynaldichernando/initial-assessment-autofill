import csv
import requests
import json
import time

if __name__ == "__main__":
    base_url = "https://api.kampusmerdeka.kemdikbud.go.id/v1alpha1/mentors/me/mentees/{}/activities/db8b3237-491e-11ec-9f02-1e6a640681ca/assessment"
    headers = {
        'Authorization': 'Bearer <token>',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44',
        'Content-Type': 'application/json'
    }

    mentees = dict()
    scores = dict()
    comments = dict()

    with open('mentees.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            mentees[row['name'].lower()] = row['id']

    with open('scores.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            scores[row['Students Name'].lower()] = (
                row['Initial Tech Scoring'], row['Initial Softskill Scoring'], row['Initial Eng Scoring'])

    with open('comments.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            comments[row['Course List']] = (
                row['Comment for score range : 90 - 70'], row['Comment for score range : 60 - 40'], row['Comment for score range : 30-10'])

    def comment_by_score(key, score):
        if int(score) >= 70:
            return comments[key][0]
        elif int(score) >= 40:
            return comments[key][1]
        else:
            return comments[key][0]

    for name, id in mentees.items():
        url = base_url.format(id)

        payload = {
            "comment": "",
            "status": "ASSESSMENT_DRAFT",
            "scores": [
                {
                    "module_id": "9c5ce808-491f-11ec-8841-ae83666665a8",
                    "module_name": "Bahasa Inggris",
                    "skill_id": "",
                    "skill_name": "",
                    "comment": comment_by_score("Bahasa Inggris", scores[name][2]),
                    "score": scores[name][2]
                },
                {
                    "module_id": "69eb76f4-4920-11ec-9f02-1e6a640681ca",
                    "module_name": "Memulai Dasar Pemrograman untuk Menjadi Pengembang Software",
                    "skill_id": "",
                    "skill_name": "",
                    "comment": comment_by_score("Memulai Dasar Pemrograman untuk Menjadi Pengembang Software", scores[name][0]),
                    "score": scores[name][0]
                },
                {
                    "module_id": "56c7e9f5-491f-11ec-9f02-1e6a640681ca",
                    "module_name": "DeepLearning.AI Tensorflow Data and Deployment",
                    "skill_id": "",
                    "skill_name": "",
                    "comment": comment_by_score("DeepLearning.AI Tensorflow Data and Deployment", scores[name][0]),
                    "score": scores[name][0]
                },
                {
                    "module_id": "53dab4dd-4920-11ec-9f02-1e6a640681ca",
                    "module_name": "Pembelajaran dan Tugas Soft skills",
                    "skill_id": "",
                    "skill_name": "",
                    "comment": comment_by_score("Pembelajaran dan Tugas Soft skills", scores[name][1]),
                    "score": scores[name][1]
                },
                {
                    "module_id": "861c0abb-491f-11ec-9f02-1e6a640681ca",
                    "module_name": "Simulasi Ujian TensorFlow Developer Certificate",
                    "skill_id": "",
                    "skill_name": "",
                    "comment": comment_by_score("Simulasi Ujian TensorFlow Developer Certificate", scores[name][0]),
                    "score": scores[name][0]
                },
                {
                    "module_id": "0617501c-491f-11ec-9f02-1e6a640681ca",
                    "module_name": "Google IT Automation with Python",
                    "skill_id": "",
                    "skill_name": "",
                    "comment": comment_by_score("Google IT Automation with Python", scores[name][0]),
                    "score": scores[name][0]
                },
                {
                    "module_id": "b258420b-491f-11ec-8841-ae83666665a8",
                    "module_name": "Review Materi",
                    "skill_id": "",
                    "skill_name": "",
                    "comment": comment_by_score("Review Materi", scores[name][1]),
                    "score": scores[name][1]
                },
                {
                    "module_id": "c7208282-491f-11ec-9f02-1e6a640681ca",
                    "module_name": "Refleksi diri",
                    "skill_id": "",
                    "skill_name": "",
                    "comment": comment_by_score("Refleksi diri", scores[name][1]),
                    "score": scores[name][1]
                },
                {
                    "module_id": "089d8423-4920-11ec-8841-ae83666665a8",
                    "module_name": "Pengenalan Ke Logika Pemrograman",
                    "skill_id": "",
                    "skill_name": "",
                    "comment": comment_by_score("Pengenalan Ke Logika Pemrograman", scores[name][0]),
                    "score": scores[name][0]
                },
                {
                    "module_id": "f521a7af-491f-11ec-8841-ae83666665a8",
                    "module_name": "Belajar Dasar Git dengan Github",
                    "skill_id": "",
                    "skill_name": "",
                    "comment": comment_by_score("Belajar Dasar Git dengan Github", scores[name][0]),
                    "score": scores[name][0]
                },
                {
                    "module_id": "dc9a6438-491f-11ec-8841-ae83666665a8",
                    "module_name": "Capstone Project / Proyek Akhir",
                    "skill_id": "",
                    "skill_name": "",
                    "comment": comment_by_score("Capstone Project / Proyek Akhir", scores[name][0]),
                    "score": scores[name][0]
                },
                {
                    "module_id": "3c09f2d2-491f-11ec-97a8-3aa4fb2c1c2f",
                    "module_name": "DeepLearning.AI TensorFlow Developer Professional Certificate",
                    "skill_id": "",
                    "skill_name": "",
                    "comment": comment_by_score("DeepLearning.AI TensorFlow Developer Professional Certificate", scores[name][0]),
                    "score": scores[name][0]
                },
                {
                    "module_id": "361a7959-4920-11ec-8841-ae83666665a8",
                    "module_name": "Persiapan Karir atau Startup",
                    "skill_id": "",
                    "skill_name": "",
                    "comment": comment_by_score("Persiapan Karir atau Startup", scores[name][1]),
                    "score": scores[name][1]
                },
                {
                    "module_id": "1e05bb7d-491f-11ec-9f02-1e6a640681ca",
                    "module_name": "Mathematics for Machine Learning",
                    "skill_id": "",
                    "skill_name": "",
                    "comment": comment_by_score("Mathematics for Machine Learning", scores[name][0]),
                    "score": scores[name][0]
                },
                {
                    "module_id": "70df08b8-491f-11ec-9f02-1e6a640681ca",
                    "module_name": "Inisiatif, Proaktif, Bertanggung jawab",
                    "skill_id": "",
                    "skill_name": "",
                    "comment": comment_by_score("Inisiatif, Proaktif, Bertanggung jawab", scores[name][1]),
                    "score": scores[name][1]
                },
                {
                    "module_id": "1f8f9a6b-4920-11ec-9f02-1e6a640681ca",
                    "module_name": "Structuring Machine Learning Projects",
                    "skill_id": "",
                    "skill_name": "",
                    "comment": comment_by_score("Structuring Machine Learning Projects", scores[name][0]),
                    "score": scores[name][0]
                }
            ]
        }

        r = requests.post(url, headers=headers, data=json.dumps(payload))

        if r.ok:
            print("Success submit for mentee: {}.".format(name))
        else:
            print("Error! (name: {})".format(name))
            break

        time.sleep(0.3)
