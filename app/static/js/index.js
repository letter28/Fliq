const playBtn = document.getElementById('play-btn');

function getCategory() {
    const categoryEl = document.getElementById('category-select');
    const allCategories = Array.from(categoryEl.children)
    const selectedCategory = allCategories[categoryEl.selectedIndex];
    const selectedCategoryText = selectedCategory.textContent;
    const selectedCategoryValue = selectedCategory.value;

    localStorage.setItem('category', selectedCategoryText);
    playBtn.href = "play-quiz/" + selectedCategoryValue
}

playBtn.addEventListener('click', getCategory);
