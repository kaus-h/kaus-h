<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/hero-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/hero-light.svg">
  <img src="./assets/hero-light.svg" alt="Kaustav Kalra — software engineer focused on systems and design" width="100%">
</picture>

<br>

i like building software where **technical depth and product design are treated as the same problem**.

my work has moved across backend systems, developer tooling, computer vision, healthcare software, AI-assisted workflows, and mobile products, but the underlying pattern lies between what a system does internally and what using it actually feels like.

| systems | product | signal |
| --- | --- | --- |
| backend architecture | interface systems | observability |
| data modeling | interaction design | metrics |
| reliability | visual language | validation |
| performance | workflow design | testing |

<sub>currently: making the invisible parts feel intentional ✦</sub>

---

## engineering telemetry

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/telemetry-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/telemetry-light.svg">
  <img src="./assets/telemetry-light.svg" alt="Engineering telemetry showing Kaustav's current technical focus" width="100%">
</picture>

<div align="center">

<img src="https://img.shields.io/github/followers/kaus-h?style=for-the-badge&logo=github&label=followers&labelColor=050509&color=FF4FD8" alt="GitHub followers">
<img src="https://img.shields.io/github/stars/kaus-h?affiliations=OWNER%2CCOLLABORATOR&style=for-the-badge&logo=github&label=stars&labelColor=050509&color=63F58B" alt="GitHub stars">

<sub>numbers, but make them pretty ♡ · #050509 / #FF4FD8 / #63F58B / #7DD3FC</sub>

</div>

<br>

<p align="center">
  <img width="49%" src="https://github-stats-extended.vercel.app/api?username=kaus-h&show_icons=true&include_all_commits=true&hide_border=true&bg_color=050509&title_color=FF4FD8&text_color=F6FAFF&icon_color=63F58B&ring_color=7DD3FC&show=reviews,prs_merged,prs_merged_percentage" alt="Kaustav's GitHub statistics">
  <img width="49%" src="https://github-stats-extended.vercel.app/api/top-langs/?username=kaus-h&layout=compact&langs_count=10&hide_border=true&bg_color=050509&title_color=7DD3FC&text_color=F6FAFF&icon_color=FF4FD8" alt="Kaustav's top languages">
</p>

<p align="center">
  <img width="72%" src="https://streak-stats.demolab.com?user=kaus-h&hide_border=true&background=050509&stroke=202634&ring=FF4FD8&fire=63F58B&currStreakNum=F6FAFF&sideNums=F6FAFF&currStreakLabel=7DD3FC&sideLabels=A7B0C0&dates=A7B0C0" alt="Kaustav's GitHub contribution streak">
</p>

<p align="center">
  <img width="100%" src="https://github-readme-activity-graph.vercel.app/graph?username=kaus-h&bg_color=050509&color=7DD3FC&line=FF4FD8&point=63F58B&area=true&area_color=7DD3FC&hide_border=true" alt="Kaustav's recent GitHub activity graph">
</p>

---

## selected systems

### [HydraScan](https://github.com/kaus-h/HydraScan)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/projects/hydrascan-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/projects/hydrascan-light.svg">
  <img src="./assets/projects/hydrascan-light.svg" alt="HydraScan project system card" width="100%">
</picture>

**on-device ML recovery intelligence for iOS.** HydraScan analyzes biomechanical movement using pose estimation and deterministic scoring, processing **33-point pose data at 120Hz** and computing **50+ biomechanical metrics**.

<details>
<summary><strong>engineering notes / architecture</strong></summary>
<br>

**Tech:** Swift, SwiftUI, MVVM, SwiftData, HealthKit, QuickPose, MediaPipe, SIMD3

- Scores squat, hip hinge, posture, balance, range of motion, and asymmetry.
- Uses NaN-safe joint-angle calculations and fallback logic for incomplete pose data.
- Built as a **12K+ line SwiftUI/MVVM client across 59 files**.
- Includes a reusable **700+ line SwiftUI design system powering 20+ views**.
- Designed as a privacy-first recovery app with deterministic scoring and on-device movement analysis.

</details>

<br>

### [BeliefGuard](https://github.com/kaus-h/BeliefGuard-Hackathon)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/projects/beliefguard-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/projects/beliefguard-light.svg">
  <img src="./assets/projects/beliefguard-light.svg" alt="BeliefGuard AI execution control project card" width="100%">
</picture>

**repository-aware execution control for AI-assisted coding.** BeliefGuard makes model assumptions explicit, grounds them against codebase evidence, and gates patch generation before workspace mutation.

<details>
<summary><strong>engineering notes / architecture</strong></summary>
<br>

**Tech:** TypeScript, VS Code Extension API, Zod, Vitest, LLM APIs

- Extracts AI agent assumptions into a typed **Repo Belief Graph**.
- Uses a **Confidence-to-Action Gate** to route changes to proceed, inspect, ask, or block.
- Integrates LLM plan extraction, workspace scanning, evidence grounding, Zod validation, structured patch generation, and per-file diff review.
- Validates behavior with Vitest, property-based tests, and benchmark scenarios.
- Built around responsible AI-assisted development, output validation, and developer trust.

</details>

<br>

### [PatientConnect360](https://github.com/kaus-h/PatientConnect360)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/projects/patientconnect360-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/projects/patientconnect360-light.svg">
  <img src="./assets/projects/patientconnect360-light.svg" alt="PatientConnect360 healthcare coordination project card" width="100%">
</picture>

**industry-sponsored healthcare coordination platform** for patients, caregivers, clinicians, and admins. Backend query improvements and pagination reduced large-dataset query time and network transfer by **~95%**.

<details>
<summary><strong>engineering notes / architecture</strong></summary>
<br>

**Tech:** React, Vite, Node.js, Express, Prisma, PostgreSQL, Recharts

- Built role-based healthcare workflows across patients, caregivers, clinicians, and admins.
- Implemented **RBAC**, OTP verification, authenticated sessions, caregiver/**MPOA** linking, privacy controls, and audit visibility.
- Developed scheduling, messaging, medication tracking, vitals, notifications, feedback, and visit lifecycle workflows.
- Built admin analytics dashboards with KPI tracking, DAU monitoring, searchable logs, filters, and pagination.
- Optimized large-dataset query time and network transfer by **95%** through pagination and backend query improvements.

</details>

---

## more work

### [RallyPoint](https://github.com/snesan821/hackathonrallypoint)

**swipeable civic discovery and action platform.** A deployed civic engagement product that helps users discover, understand, and act on local policy issues.

**Tech:** Next.js, TypeScript, Prisma, PostgreSQL, Redis, Clerk, Claude

- Built feed, saved, profile, discussion, and issue-tracking workflows.
- Implemented **Redis-backed state consistency and low-latency APIs**.
- Built personalized ranking using interests, district matching, geography, and engagement velocity.
- Integrated Claude-powered summarization for dense civic issue content.

### Play Music to Tune Up Your Mood

**published AI/ML research project.** A machine-learning project using Spotify API data to classify songs by emotional tone, reaching **76 percent classification accuracy**.

**Tech:** Python, Keras, scikit-learn, Pandas, NumPy, Seaborn, Matplotlib, Spotify API

- Built a neural network for music emotion classification.
- Used feature preprocessing, scaling, label encoding, K-Fold cross validation, and confusion-matrix reporting.
- Published findings on acousticness, valence, tempo, and emotional tone classification.

---

## stack / toolbox

| languages | systems + data | product | intelligence + data | quality + workflow |
| --- | --- | --- | --- | --- |
| TypeScript | Node.js | React | LLM APIs | Git |
| JavaScript | Express | Next.js | Claude | GitHub |
| Python | REST APIs | Vite | Gemini | VS Code |
| Java | PostgreSQL | Tailwind CSS | Keras | Vitest |
| C++ | MySQL | SwiftUI | scikit-learn | Zod |
| Swift | Prisma |  | Pandas | JUnit |
| SQL | Redis |  | NumPy |  |

<details>
<summary><strong>full technology index</strong></summary>
<br>

**Languages** — TypeScript, JavaScript, Python, Java, C++, Swift, SQL

**Frontend / product** — React, Next.js, Vite, Tailwind CSS, SwiftUI

**Backend, APIs, databases** — Node.js, Express, REST APIs, PostgreSQL, MySQL, Prisma, Redis

**AI, ML, data** — LLM APIs, Claude, Gemini, Keras, scikit-learn, Pandas, NumPy

**Tools + workflow** — Git, GitHub, VS Code, Vitest, Zod, JUnit

</details>

---

## current signal

**what i like building**

- Full-stack applications with real users and clear workflows.
- AI-assisted tools that improve developer productivity and trust.
- Healthcare and clinical workflow software.
- Internal tools, dashboards, and automation systems.
- Data-driven applications with SQL-backed models.
- Frontend experiences that make complex systems easier to use.
- Reliable APIs, validation layers, and testable software.

**what i'm going deeper on**

- AI automation and LLM-powered workflows.
- Full-stack product engineering with React, TypeScript, and PostgreSQL.
- Backend API design and data modeling.
- Testing, validation, and software quality.
- Cloud fundamentals and deployment workflows.
- Healthcare, education, and developer tooling products.
- Workflow automation, observability, and reliable software systems.

---

## experience

| | role | signal |
| --- | --- | --- |
| **iDTech Camps** | On-Campus Instructor | Java · 3D printing · character modeling · video · ethical AI |
| **On My Own Technology** | Research Intern | Python · Keras · Spotify API · music emotion classification |
| **IndianRaga** | Social Media Marketing Intern | Google Analytics · AdSense · YouTube · Instagram · Facebook |

<details>
<summary><strong>experience notes</strong></summary>
<br>

### On-Campus Instructor, iDTech Camps
Taught Java programming, 3D printing, character modeling, video production, and ethical AI through hands-on student projects.

### Research Intern, On My Own Technology
Researched music emotion classification and built a Keras/Spotify API machine learning model with Python and scikit-learn.

### Social Media Marketing Intern, IndianRaga
Analyzed Google Analytics, AdSense, YouTube, Instagram, and Facebook performance data to support growth and content optimization.

</details>

---

## about / full snapshot

Computer Science graduate with a concentration in **Software Engineering from Arizona State University**.

My background spans full-stack software engineering, AI-assisted developer tools, healthcare technology, data-driven applications, and product-focused engineering. I enjoy building practical software that connects clean interfaces, reliable backend systems, structured data, and thoughtful user workflows.

<details>
<summary><strong>original profile details, preserved</strong></summary>
<br>

- Computer Science graduate with a concentration in Software Engineering from Arizona State University.
- Interested in full-stack engineering, frontend/product engineering, AI automation, healthcare software, internal tools, and data-driven systems.
- Strongest technologies: TypeScript, JavaScript, React, Node.js, Express, PostgreSQL, Python, Swift, SQL, Git, and REST APIs.
- I like building products end to end, from user flows and UI to APIs, databases, validation, testing, and documentation.
- Currently exploring AI-assisted development, LLM workflows, workflow automation, observability, and reliable software systems.

```text
Primary Focus: Full-stack software engineering, AI tools, healthcare/product workflows
Frontend: React, Next.js, TypeScript, JavaScript, Tailwind CSS, SwiftUI
Backend: Node.js, Express, REST APIs, Prisma, PostgreSQL, MySQL, Redis
AI/ML: LLM APIs, Claude, Gemini, Keras, scikit-learn, Pandas, NumPy
Quality: Vitest, Zod, JUnit, validation, debugging, documentation
Interests: AI automation, healthtech, education technology, developer tools, internal tools
```

Legacy portfolio link from the previous profile: [Website](linkedin.com/in/kaustavkalra/)

</details>

---

<div align="center">

### Kaustav Kalra

**software engineer · systems + design**

[linkedin](https://www.linkedin.com/in/kaustavkalra/) · [github](https://github.com/kaus-h)

<sub>phoenix / arizona · small signal, big system ✦</sub>

</div>
