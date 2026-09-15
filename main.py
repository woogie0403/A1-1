import json
import os

# -------------------------------------------------------------
# 파일 경로 및 기본 프롬프트 데이터
# -------------------------------------------------------------
DATA_FILE = "prompts.json"
EXPORT_MD_FILE = "prompts_by_category.md"

DEFAULT_PROMPTS = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요. 서론, 본론, 결론 구조를 갖추고 매력적인 제목을 제안해주세요.",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "제품 썸네일 생성",
        "content": "다음 제품의 매력적인 썸네일 이미지를 생성해주세요. 모던하고 미니멀한 스타일, 자연광 조명, 4K 고화질 배경을 반영해주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": "당신은 글로벌 IT 컨설팅 회사의 수석 컨설턴트입니다. 클라이언트의 요구사항을 분석하여 비즈니스 가치 중심의 디지털 전환 전략을 조언해주세요.",
        "category": "페르소나",
        "favorite": False
    }
]

CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]


def load_prompts():
    """JSON 파일에서 프롬프트 불러오기 (없으면 기본 데이터 반환)"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                print(f"[안내] '{DATA_FILE}' 파일에서 {len(data)}개의 프롬프트를 불러왔습니다.")
                return data
        except Exception as e:
            print(f"[경고] 파일 불러오기 실패: {e}")
    return list(DEFAULT_PROMPTS)


def save_prompts(prompts_list):
    """프롬프트 데이터를 JSON 파일로 저장하기"""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(prompts_list, f, ensure_ascii=False, indent=4)
        print(f"[성공] 프롬프트 데이터가 '{DATA_FILE}' 파일에 안전하게 저장되었습니다.")
    except Exception as e:
        print(f"[오류] 저장 실패: {e}")


def export_to_markdown(prompts):
    """전체 프롬프트를 카테고리별 Markdown 파일로 내보내기 (보너스 과제)"""
    print("\n=== Markdown 파일로 내보내기 ===")
    if not prompts:
        print("내보낼 프롬프트가 없습니다.")
        return

    # 1. 카테고리별로 프롬프트 묶기(그룹화)
    grouped = {}
    for p in prompts:
        cat = p.get("category", "기타")
        if cat not in grouped:
            grouped[cat] = []
        grouped[cat].append(p)

    # 2. 마크다운 파일 작성
    try:
        with open(EXPORT_MD_FILE, "w", encoding="utf-8") as f:
            f.write("# 📚 나만의 프롬프트 모음집 (카테고리별)\n\n")
            f.write("> 이 문서는 프롬프트 관리 프로그램에서 자동으로 추출(Export)된 파일입니다.\n\n")

            for cat, items in grouped.items():
                f.write(f"## 📁 {cat} ({len(items)}개)\n\n")
                for idx, p in enumerate(items, 1):
                    fav_mark = " (★ 즐겨찾기)" if p.get("favorite") else ""
                    f.write(f"### {idx}. {p['title']}{fav_mark}\n\n")
                    f.write("```text\n")
                    f.write(f"{p['content']}\n")
                    f.write("```\n\n")

        print(f"[성공] 모든 프롬프트가 '{EXPORT_MD_FILE}' 파일로 성공적으로 내보내졌습니다!")
    except Exception as e:
        print(f"[오류] 내보내기 실패: {e}")


def show_menu():
    """메인 메뉴 출력 함수"""
    print("\n" + "=" * 25)
    print("=== 나만의 프롬프트 관리 ===")
    print("=" * 25)
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. JSON 파일로 저장")
    print("9. Markdown 파일로 내보내기")
    print("0. 종료")
    print("=" * 25)


def add_prompt(prompts):
    """새로운 프롬프트 등록 함수"""
    print("\n=== 프롬프트 추가 ===")

    while True:
        title = input("제목: ").strip()
        if title:
            break
        print("[오류] 제목은 비워둘 수 없습니다. 다시 입력해주세요.")

    while True:
        content = input("내용: ").strip()
        if content:
            break
        print("[오류] 내용은 비워둘 수 없습니다. 다시 입력해주세요.")

    print("\n카테고리 선택:")
    for idx, cat in enumerate(CATEGORIES, 1):
        print(f"{idx}) {cat}")

    while True:
        cat_choice = input("선택 (번호 1~6 또는 직접 입력): ").strip()
        if not cat_choice:
            print("[오류] 카테고리를 선택하거나 입력해주세요.")
            continue

        if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(CATEGORIES):
            category = CATEGORIES[int(cat_choice) - 1]
            break
        else:
            category = cat_choice
            break

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }
    prompts.append(new_prompt)
    print("\n프롬프트가 성공적으로 추가되었습니다!")
    save_prompts(prompts)


def show_list(prompts):
    """저장된 모든 프롬프트 목록 출력 함수"""
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for idx, p in enumerate(prompts, 1):
        fav_mark = "☆" if p.get("favorite") else ""
        print(f"{idx}. [{p['category']}] {p['title']}{fav_mark}")

    print(f"총 {len(prompts)}개의 프롬프트")


def show_detail(prompts):
    """프롬프트 상세 내용 보기 함수"""
    print("\n=== 프롬프트 상세 보기 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    num_str = input("번호 입력: ").strip()
    if not num_str.isdigit() or not (1 <= int(num_str) <= len(prompts)):
        print("[오류] 유효한 프롬프트 번호를 입력해주세요.")
        return

    idx = int(num_str) - 1
    p = prompts[idx]
    fav_mark = "☆" if p.get("favorite") else "없음"

    print(f"\n제목: {p['title']}")
    print(f"카테고리: {p['category']}")
    print(f"즐겨찾기: {fav_mark}")
    print("내용:")
    print(p['content'])


def manage_favorite(prompts):
    """즐겨찾기 추가/해제 토글 함수"""
    print("\n=== 즐겨찾기 관리 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    num_str = input("프롬프트 번호 입력: ").strip()
    if not num_str.isdigit() or not (1 <= int(num_str) <= len(prompts)):
        print("[오류] 유효한 프롬프트 번호를 입력해주세요.")
        return

    idx = int(num_str) - 1
    p = prompts[idx]

    p["favorite"] = not p.get("favorite", False)

    if p["favorite"]:
        print(f"'{p['title']}' 프롬프트를 즐겨찾기에 추가했습니다! ☆")
    else:
        print(f"'{p['title']}' 프롬프트를 즐겨찾기에서 해제했습니다.")

    save_prompts(prompts)


def show_favorites(prompts):
    """즐겨찾기된 프롬프트만 출력하는 함수"""
    print("\n=== 즐겨찾기 목록 ===")
    fav_list = [p for p in prompts if p.get("favorite")]

    if not fav_list:
        print("즐겨찾기로 등록된 프롬프트가 없습니다.")
        return

    for idx, p in enumerate(fav_list, 1):
        print(f"{idx}. [{p['category']}] {p['title']}☆")

    print(f"총 {len(fav_list)}개의 즐겨찾기")


def filter_by_category(prompts):
    """카테고리별 프롬프트 조회 함수"""
    print("\n=== 카테고리별 조회 ===")
    print("카테고리 선택:")
    for idx, cat in enumerate(CATEGORIES, 1):
        print(f"{idx}) {cat}")

    choice = input("선택 (번호 1~6 또는 직접 입력): ").strip()
    if not choice:
        print("[오류] 카테고리를 입력해주세요.")
        return

    if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
        target_cat = CATEGORIES[int(choice) - 1]
    else:
        target_cat = choice

    filtered = [p for p in prompts if p.get("category") == target_cat]

    print(f"\n[{target_cat}] 카테고리 프롬프트:")
    if not filtered:
        print("해당 카테고리에 등록된 프롬프트가 없습니다.")
        return

    for idx, p in enumerate(filtered, 1):
        fav_mark = "☆" if p.get("favorite") else ""
        print(f"{idx}. {p['title']}{fav_mark}")

    print(f"총 {len(filtered)}개의 프롬프트")


def search_prompt(prompts):
    """키워드로 제목 또는 내용 검색 함수"""
    print("\n=== 프롬프트 검색 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    keyword = input("검색어: ").strip()
    if not keyword:
        print("[오류] 검색어를 입력해주세요.")
        return

    results = [
        p for p in prompts
        if keyword.lower() in p["title"].lower() or keyword.lower() in p["content"].lower()
    ]

    print("\n검색 결과:")
    if not results:
        print("검색 결과가 없습니다.")
        return

    for idx, p in enumerate(results, 1):
        fav_mark = "☆" if p.get("favorite") else ""
        print(f"{idx}. [{p['category']}] {p['title']}{fav_mark}")

    print(f"{len(results)}개의 프롬프트를 찾았습니다.")


def main():
    """프로그램 메인 루프"""
    prompts = load_prompts()

    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            add_prompt(prompts)
        elif choice == "2":
            show_list(prompts)
        elif choice == "3":
            filter_by_category(prompts)
        elif choice == "4":
            search_prompt(prompts)
        elif choice == "5":
            show_detail(prompts)
        elif choice == "6":
            manage_favorite(prompts)
        elif choice == "7":
            show_favorites(prompts)
        elif choice == "8":
            save_prompts(prompts)
        elif choice == "9":
            export_to_markdown(prompts)
        elif choice == "0":
            save_prompts(prompts)
            print("\n프로그램을 종료합니다. 이용해주셔서 감사합니다!")
            break
        else:
            print("\n[오류] 올바른 번호를 입력해주세요 (0~9).")


if __name__ == "__main__":
    main()