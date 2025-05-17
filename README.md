# fastapi-cicdct-workshop
A Workshop for Python course about FastAPI, CI-CD-CT with Python

# Installation
1. First create a virtual environment and install all necessary packages from requirements.txt
```
python -m venv .venv
venv\Scripts\activate
pip install -r requirements.txt
```
2. Run the project with:
```
uvicorn main:app --reload
```

# Main goal of the Workshop (in Azerbaijani)
# FastAPI Workshop: Sadə Konvertasiya API-si və Testlər ilə CI

Bu praktik workshop-da biz **FastAPI** ilə sadə Python veb API yaradacaq, avtomatlaşdırılmış testlər yazacaq və **GitHub Actions** ilə Davamlı İnteqrasiya (CI) quracağıq.

---

## 🎯 Workshop-un Məqsədi

Bu workshop-un əsas məqsədləri:

- Pydantic kimi əlavə kitabxanalara ehtiyac olmadan FastAPI ilə minimal REST API qurmaq.
- API endpoint-ləri üçün `pytest` və FastAPI-nin `TestClient` modulundan istifadə edərək vahid testlər yazmaq.
- Kodun test əhatə dairəsini (coverage) ölçmək və hesabat hazırlamaq.
- GitHub Actions vasitəsilə hər push və pull request zamanı testlərin avtomatik işə düşməsini təmin etmək.
- CI workflow-da test coverage hesabatını yüklənə bilən artefakt kimi saxlamaq.

Workshop əsasən backend inkişafı, test avtomatlaşdırması və DevOps (xüsusilə CI/CD) mövzularına maraq göstərən proqramçılar üçün nəzərdə tutulub.

---

## 🛠 Nə Quruldu?

- **FastAPI tətbiqi:**  
  İki endpoint-dən ibarət sadə API:
  - `GET /` — Xoş gəldiniz mesajı.
  - `POST /convert` — Selsi ilə Farenheit arasında temperatur konvertasiyası.

- **Testlər:**  
  Aşağıdakı halları əhatə edən vahid testlər:
  - `GET /` endpoint-in cavabının yoxlanması.
  - Temperaturun düzgün konvertasiya olunması.
  - Yanlış və ya əskik parametrlərin düzgün işlənməsi.

- **Kod əhatə dairəsi (Coverage):**  
  Testlər HTML formatında vizual kod əhatə hesabatı yaradır.

- **GitHub Actions ilə CI:**  
  Hər dəfə `main` branch-a push və ya pull request zamanı:
  - Requirement'lər quraşdırılır.
  - Testlər işə düşür və coverage ölçülür.
  - Coverage hesabatı artefakt kimi endirilə bilir.

---
