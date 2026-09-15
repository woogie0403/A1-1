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

    # 1. 제목 입력 및 비어있는지 검증
    while True:
        title = input("제목: ").strip()
        if title:
            break
        print("[오류] 제목은 비워둘 수 없습니다. 다시 입력해주세요.")

    # 2. 내용 입력 및 비어있는지 검증
    while True:
        content = input("내용: ").strip()
        if content:
            break
        print("[오류] 내용은 비워둘 수 없습니다. 다시 입력해주세요.")

    # 3. 카테고리 선택 또는 직접 입력
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
            # 직접 텍스트로 카테고리를 입력한 경우
            category = cat_choice
            break

    # 4. 프롬프트 데이터 딕셔너리 생성 및 리스트 추가 (즐겨찾기 기본값: False)
    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }
    prompts.append(new_prompt)
    print("\n프롬프트가 성공적으로 추가되었습니다!")


def main():
    """프로그램 메인 루프"""
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            print("\n[안내] 프롬프트 목록 기능은 다음 단계(브랜치 미션)에서 구현됩니다.")
        elif choice == "3":
            print("\n[안내] 카테고리별 조회 기능은 다음 단계에서 구현됩니다.")
        elif choice == "4":
            print("\n[안내] 프롬프트 검색 기능은 다음 단계에서 구현됩니다.")
        elif choice == "5":
            print("\n[안내] 프롬프트 상세 보기 기능은 다음 단계에서 구현됩니다.")
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