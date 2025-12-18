# Rick and Morty – Characters Collector

פרויקט זה מדגים איסוף נתונים מ־**Rick and Morty API**, שמירתם לקובץ CSV, חשיפת הנתונים דרך REST API, והרצה באמצעות **Docker**, **Kubernetes**, ו־**Helm**. בנוסף, קיים Pipeline של **GitHub Actions** לבנייה ופריסה אוטומטית.

---

## 🎯 מטרת הפרויקט

לאסוף את כל הדמויות שעומדות בתנאים:

* Species = **Human**
* Status = **Alive**
* Origin = **Earth**

ולשמור עבור כל דמות:

* Name
* Location
* Image link

---

## 📁 מבנה הפרויקט

```
.
├── app/
│   ├── main.py            # REST API (FastAPI)
│   ├── fetch_data.py      # סקריפט לאיסוף הנתונים מה־API
│   └── data.csv           # קובץ תוצאות
│
├── Dockerfile
├── requirements.txt
├── yamls/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
│
├── helm/
│   └── rick-morty-chart/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
│           ├── deployment.yaml
│           ├── service.yaml
│           └── ingress.yaml
│
├── .github/workflows/
│   └── ci-cd.yaml
│
└── README.md
```

---

## 🐍 שלב 1 – איסוף הנתונים

### fetch_data.py

* מבצע Pagination מול Rick and Morty API
* מסנן לפי התנאים
* שומר את הנתונים לקובץ `data.csv`

פורמט הקובץ:

```
Name,Location,Image
Rick Sanchez,Earth,https://rickandmortyapi.com/api/character/avatar/1.jpeg
```

הרצה מקומית:

```bash
python fetch_data.py
```

---

## 🌐 שלב 2 – REST API

ה־API נכתב ב־**FastAPI**.

### Endpoints

| Method | Endpoint     | Description                |
| ------ | ------------ | -------------------------- |
| GET    | /characters  | מחזיר את כל הדמויות כ־JSON |
| GET    | /healthcheck | בדיקת תקינות השירות        |

דוגמה:

```bash
curl http://localhost:8000/characters
```

---

## 🐳 Docker

### בניית Image

```bash
docker build -t rick-morty-app .
```

### הרצה

```bash
docker run -p 8000:8000 rick-morty-app
```

בדיקה:

```bash
curl http://localhost:8000/healthcheck
```

---

## ☸️ Kubernetes (Minikube / MicroK8s)

### פריסה עם YAML

```bash
kubectl apply -f yamls/
```

בדיקה:

```bash
kubectl get pods
kubectl get svc
```

גישה לשירות (Minikube):

```bash
minikube service rick-morty-service
```

---

## ⎈ Helm Deployment

### התקנת Helm Chart

```bash
helm install rick-morty ./helm/rick-morty-chart
```

### עדכון

```bash
helm upgrade rick-morty ./helm/rick-morty-chart
```

### הסרה

```bash
helm uninstall rick-morty
```

---

## 🤖 GitHub Actions – CI/CD

Pipeline כולל:

1. Checkout לקוד
2. Build ל־Docker Image
3. הקמת Cluster מקומי (Kind)
4. Deploy ל־Kubernetes
5. בדיקות Healthcheck ו־API

ה־workflow נמצא ב:

```
.github/workflows/ci-cd.yaml
```

לאחר מתן **Read Access** ל־`chene@elementor.com`, ניתן לצפות בפלט הריצה ב־GitHub Actions.

---

## ✅ דרישות מוקדמות

* Python 3.9+
* Docker
* kubectl
* Helm
* Minikube / MicroK8s

---

## 🧪 בדיקות מהירות

```bash
curl http://localhost:8000/healthcheck
curl http://localhost:8000/characters
```

---

## 📌 הערות

* הנתונים נטענים מקובץ CSV (ניתן להחליף ל־DB בעתיד)
* הפרויקט בנוי כ־Service עצמאי ו־Cloud-Native

---

בהצלחה 🚀
