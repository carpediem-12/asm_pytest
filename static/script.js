// 정답 설정 (여기선 "Hello, World!"로 테스트)
const correctAnswer = "Hello, World!";

// 버튼 클릭 이벤트 설정
document.getElementById("check-answer-btn").addEventListener("click", function() {
    // 사용자가 입력한 값 가져오기
    const userAnswer = document.getElementById("user-answer").value.trim();
    
    // 결과 출력 요소 선택
    const resultElement = document.getElementById("result");
    
    // 입력과 정답 비교
    if (userAnswer === correctAnswer) {
        resultElement.textContent = "🎉 정답입니다! 축하합니다!";
        resultElement.style.color = "lime";
    } else {
        resultElement.textContent = "❌ 틀렸습니다. 다시 시도해보세요!";
        resultElement.style.color = "red";
    }
});
