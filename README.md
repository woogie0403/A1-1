# 🚀 나만의 프롬프트 관리 프로그램 (Prompt Manager)

AI 프롬프트(텍스트, 이미지, 페르소나 등)를 체계적으로 등록, 분류, 검색, 관리할 수 있는 파이썬 콘솔 기반 소프트웨어입니다.  
Python 기초 문법(자료구조, 제어문, 함수 분리)과 Git 형상 관리(기능 단위 커밋, 브랜치 분기 및 병합)를 실습하고 적용한 프로젝트입니다.

---

## 🛠️ 1. 개발 환경 및 Git 설정

실제 과제를 수행하고 검증한 로컬 개발 환경 정보입니다.

- **Python 버전**: Python 3.14.7 (Python 3.10 이상 요구조건 충족)
- **Git 버전**: `git version 2.55.0.windows.4`
- **Git 사용자 설정**:
  - `user.name`: `woogie0403`
  - `user.email`: `jaewook0403@gmail.com`
- **저장소 URL**: [https://github.com/woogie0403/A1-1](https://github.com/woogie0403/A1-1)
- **기본 브랜치**: `main`
- **외부 라이브러리**: 내장 표준 라이브러리(`json`, `os`)만 사용 (외부 의존성 없음)

---

## 📌 2. 주요 기능 목록

1. **프롬프트 추가 (`add_prompt`)**: 제목, 내용, 카테고리를 입력받아 신규 프롬프트 등록 (빈값 입력 시 재입력 유효성 검사)
2. **프롬프트 목록 조회 (`show_list`)**: 등록된 전체 프롬프트의 번호, 카테고리, 제목, 즐겨찾기 여부(★) 확인 (*별도 기능 브랜치에서 개발 후 병합*)
3. **카테고리별 조회 (`filter_by_category`)**: 카테고리를 선택하여 해당 분류에 속한 프롬프트만 필터링하여 출력
4. **프롬프트 검색 (`search_prompt`)**: 키워드를 입력받아 제목 또는 내용에 포함된 프롬프트를 검색 (대소문자 무시)
5. **프롬프트 상세 보기 (`show_detail`)**: 프롬프트 번호를 입력받아 제목, 카테고리, 즐겨찾기 상태, 전체 본문 출력
6. **즐겨찾기 관리 (`manage_favorite`)**: 프롬프트 번호를 입력하여 즐겨찾기를 추가하거나 해제 (토글 방식)
7. **즐겨찾기 목록 (`show_favorites`)**: 즐겨찾기(★)로 등록된 프롬프트만 모아서 확인
8. **데이터 영속화 [보너스] (`save_prompts`, `load_prompts`)**: `prompts.json` 파일 입출력을 통해 프로그램 종료 후 재실행해도 데이터 영구 보존
9. **Markdown 내보내기 [보너스] (`export_to_markdown`)**: 전체 프롬프트를 카테고리별 마크다운 문서(`prompts_by_category.md`)로 자동 추출
10. **프로그램 종료**: 메뉴에서 `0`번 선택 시 안전하게 프로세스 종료

---

## 🏗️ 3. 프로그램 구조 및 설계 내용

### (1) 데이터 구조: List와 Dictionary의 조합
- **구조**: `prompts = [ { "title": "...", "content": "...", "category": "...", "favorite": False }, ... ]`
- **선택 이유**:
  - **리스트(`List`)**: 여러 프롬프트 데이터의 등록 순서를 안정적으로 유지하고, 1번부터 매핑되는 인덱스를 기반으로 목록 출력과 선택을 직관적으로 처리하기 위해 사용했습니다.
  - **딕셔너리(`Dictionary`)**: 개별 프롬프트가 가지는 속성(`title`, `content`, `category`, `favorite`)을 명확한 Key-Value 쌍으로 관리하여 `p["title"]`이나 `p.get("favorite", False)` 형태로 가독성과 안정성을 확보했습니다.

### (2) 메인 루프 및 종료 조건 설계
- 프로그램 실행 시 `while True` 무한 루프를 사용하여 사용자가 의도적으로 종료하기 전까지 대화형 메뉴를 계속 유지합니다.
- 메뉴 입력값으로 `0`이 들어오면 루프를 탈출(`break`)하여 안전하게 종료되며, 허용 범위 밖의 숫자나 잘못된 입력이 들어오면 오류 메시지를 띄우고 다시 메뉴를 출력합니다.

### (3) 함수 분리 및 단일 책임 원칙
- 프로그램의 모든 기능을 한 곳에 몰아넣지 않고, 메뉴 출력(`show_menu`), 추가(`add_prompt`), 목록(`show_list`), 검색(`search_prompt`), 파일 입출력(`save_prompts`, `load_prompts`) 등으로 명확히 역할을 분리하여 코드 가독성과 유지보수성을 높였습니다.

---

## 🌿 4. Git 형상 관리 및 브랜치 실습 이력

### (1) 기능 단위 커밋 (Atomic Commit) 원칙
- 전체 코드를 한 번에 커밋하지 않고, 각 기능 구현 및 문서화 단계마다 명확한 접두사(`feat:`, `docs:`, `fix:`, `merge:`)를 사용하여 총 15회의 기능 단위 커밋을 기록했습니다.

### (2) 브랜치 분기 및 병합 실습
- **브랜치 분기**: 프롬프트 목록 보기 기능 구현을 위해 `main` 브랜치에서 `feature/list` 브랜치를 분기(`git checkout -b feature/list`)하여 독립적으로 작업을 진행했습니다.
- **기능 병합**: 기능 완성 후 `main` 브랜치로 이동하여 `feature/list` 브랜치를 병합(`git merge feature/list`)하여 이력을 남겼습니다.

### (3) 실제 Git 커밋 및 병합 히스토리 (`git log --oneline --graph`)
```text
* c957165 docs: 보너스 과제 실행 결과 증빙 스크린샷 추가
* de52123 docs: 보너스 기능(JSON 영속화, MD 내보내기) 설명 추가
* f4b6d24 feat: 카테고리별 Markdown 문서 내보내기 기능 구현 (export_to_markdown)
* 9f092fd feat: JSON 파일 입출력을 통한 프롬프트 영속화 구현 (save/load)
* 54ad679 fix: 스크린샷 파일명 수정
* ad2f970 docs: 과제 증빙 스크린샷 추가
* 90839c5 docs: 프로그램 기능 및 실행 방법 상세 README.md 작성
* ea5e1e9 feat: 키워드 검색 기능 구현 (search_prompt)
* 8cd12e0 feat: 카테고리별 조회 기능 구현 (filter_by_category)
* 5952a49 feat: 즐겨찾기 관리 및 즐겨찾기 목록 조회 구현 (manage_favorite, show_favorites)
* f41ec3b feat: 프롬프트 상세 보기 기능 구현 (show_detail)
*   2b3eb3f merge: feat/list 브랜치 병합 (목록 조회 기능)
|\  
| * 412ba3a feat: 프롬프트 목록 조회 기능 구현 (show_list)
|/  
* 833eb33 feat: 프롬프트 추가 기능 구현 (add_prompt)
* 6ee9d07 feat: 프로그램 뼈대 및 기본 프롬프트 데이터 구조 구현
```

---

## 📂 5. 지원 카테고리 안내

- `텍스트 생성`: 블로그 글, 이메일, 보고서 등 텍스트 작성을 돕는 프롬프트
- `이미지 생성`: Midjourney, DALL-E 등 이미지 생성용 고화질 묘사 프롬프트
- `영상 생성`: 광고 스크립트, 영상 스토리보드 기획용 프롬프트
- `페르소나`: 전문가, 컨설턴트 등 특정 직무의 역할을 부여하는 프롬프트
- `자동화`: 뉴스 요약, 데이터 전처리, 노코드 연동 프롬프트
- `기타`: 사용자가 직접 입력한 커스텀 카테고리

---

## 💻 6. 실행 방법

### 저장소 클론 및 실행
```bash
git clone https://github.com/woogie0403/A1-1.git
cd A1-1
python main.py
```

---

## 📸 7. 과제 수행 증빙 스크린샷

### 1. 개발 환경 설정
![환경설정](screenshots/1_env.png)

### 2. 프로그램 실행 결과
![실행결과](screenshots/2_execution.png)

### 3. Git Graph (브랜치 및 커밋 이력)
![깃그래프](screenshots/3_git_graph.png)

### 4. 보너스 과제 실행 결과 (JSON 영속화 및 Markdown 내보내기)
![보너스과제](screenshots/4_bonus.png)