document.addEventListener('DOMContentLoaded', function () {

    let variableStar = 5;
    displayReviews(variableStar);

    document.getElementById("dropdownMenuButton").onclick = function () {
        const buttons = document.getElementsByClassName("dropdown-item");
        const dropdown = document.getElementById("dropdownText");
        for (let i = 0; i < buttons.length; i++) {
            buttons[i].addEventListener('click', function () {
            variableStar = parseInt(buttons[i].innerHTML);
            if ([1,2,3,4,5].includes(variableStar)) {
                displayReviews(variableStar);
            } else {
                displayReviews('All');
            }
            dropdown.innerHTML = buttons[i].innerHTML;
        });
        }
    };

    function displayReviews(varStar) {
        console.log(`varStar = ${varStar}`);
        let filterList = document.getElementById('filterList');
        filterList.innerHTML = "";
        if(varStar == 'All' || isNaN(varStar)){
            listofReviews.sort((a, b) => b.fields.stars - a.fields.stars);
            for(let review of listofReviews){
                let li = document.createElement("li");
                let firstname = review.fields.firstname;
                let lastname = review.fields.lastname;
                if (!lastname){
                    lastname = " ";
                }
                let stars = review.fields.stars;
                let description = review.fields.description;
                reviewCard = `
                    <div class="card">
                    <h2>${firstname} ${lastname}</h2><br>
                    <h3>${"★".repeat(stars)}</h3>
                    <p>
                        ${description}
                    </p>
                </div><br>`;
                filterList.appendChild(li).innerHTML = reviewCard;
            }
        }
        for (let review of listofReviews) {
            let li = document.createElement("li");
            let firstname = review.fields.firstname;
            let lastname = review.fields.lastname;
            if (!lastname){
                lastname = "";
            }
            let stars = review.fields.stars;
            let description = review.fields.description;
            reviewCard = `
                <div class="card">
                <h2>${firstname}  ${lastname}</h2><br>
                <h3>${"★".repeat(stars)}</h3>
                <p>
                    ${description}
                </p>
            </div><br>`;
            if (stars == varStar) {
                filterList.appendChild(li).innerHTML = reviewCard;
            }
        }
    }
});
