# -------------------------------------------------------------
# 기본 프롬프트 데이터
# -------------------------------------------------------------
prompts = [
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
    print("0. 종료")
    print("=" * 25)


def add_prompt():
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


def show_list():
    """저장된 모든 프롬프트 목록 출력 함수"""
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for idx, p in enumerate(prompts, 1):
        fav_mark = "☆" if p.get("favorite") else ""
        print(f"{idx}. [{p['category']}] {p['title']}{fav_mark}")

    print(f"총 {len(prompts)}개의 프롬프트")


def show_detail():
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


def main():
    """프로그램 메인 루프"""
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            print("\n[안내] 카테고리별 조회 기능은 다음 단계에서 구현됩니다.")
        elif choice == "4":
            print("\n[안내] 프롬프트 검색 기능은 다음 단계에서 구현됩니다.")
        elif choice == "5":
            show_detail()
        elif choice == "6":
            print("\n[안내] 즐겨찾기 관리 기능은 다음 단계에서 구현됩니다.")
        elif choice == "7":
            print("\n[안내] 즐겨찾기 목록 기능은 다음 단계에서 구현됩니다.")
        elif choice == "0":
            print("\n프로그램을 종료합니다. 이용해주셔서 감사합니다!")
            break
        else:
            print("\n[오류] 올바른 번호를 입력해주세요 (0~7).")


if __name__ == "__main__":
    main()