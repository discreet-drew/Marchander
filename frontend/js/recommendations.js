console.log("recommendations.js loaded");

function renderRecommendations(list){

    const container =
        document.getElementById("recommendations");

    if(!container) return;

    container.innerHTML = "";

    if(!list || list.length===0){

        container.innerHTML =

        `
        <div class="recommendation-empty">

            <h3>No Recommendations</h3>

            <p>

                Search more products to improve AI recommendations.

            </p>

        </div>
        `;

        return;

    }

    let html =

    `
    <h2 class="recommendation-title">

        AI Recommendations

    </h2>

    <div class="recommendation-grid">
    `;

    console.log("Rendering recommendations:");
    console.log(list);

    list.forEach(item=>{

    console.log(item);

    let product="";

    if(typeof item==="string"){

        product=item;

    }

    else if(typeof item.product==="string"){

        product=item.product;

    }

    else if(item.product && typeof item.product==="object"){

        product=item.product.title || "";

    }

    else if(item.title){

        product=item.title;

    }

    else{

        product=JSON.stringify(item);

    }

    const safeProduct=String(product).replace(/'/g,"\\'");

    html+=`

    <div class="recommendation-card">

        <h3>${product}</h3>

        <button
        onclick="searchRecommendation('${safeProduct}')">

            Compare Prices

        </button>

    </div>

    `;

    });

    html += "</div>";

    container.innerHTML = html;

}

function renderSuggestions(suggestions){

    const div =
        document.getElementById("suggestions");

    if(!div) return;

    div.innerHTML="";

    if(!suggestions || suggestions.length===0){

        div.style.display="none";

        return;

    }

    div.style.display="block";

    let html="";

    suggestions.forEach(item=>{

        let product = "";

        if(typeof item === "string"){

            product = item;

        }
        else if(item.product){

            if(typeof item.product === "string"){

                product = item.product;

            }
            else{

                product = item.product.title || "";

            }

        }
        else{

            product = item.title || "";

        }

        html +=

        `
        <div
            class="suggestion-item"

            onclick="selectSuggestion('${product.replace(/'/g,"\\'")}')">

             ${product}

        </div>
        `;

    });

    div.innerHTML=html;

}

function selectSuggestion(product){

    document
        .getElementById("query")
        .value = product;

    document
        .getElementById("suggestions")
        .style.display="none";

}

async function searchRecommendation(product){

    document
        .getElementById("query")
        .value = product;

    await searchProduct();

}

function showRecommendationLoading(){

    const div =
        document.getElementById("recommendations");

    if(!div) return;

    div.innerHTML=

    `
    <div class="recommendation-loading">

        Finding Similar Products...

    </div>
    `;

}

function hideSuggestions(){

    const div =
        document.getElementById("suggestions");

    if(div){

        div.style.display="none";

    }

}

document.addEventListener("click",function(event){

    const input =
        document.getElementById("query");

    const suggestionBox =
        document.getElementById("suggestions");

    if(!input || !suggestionBox) return;

    if(

        event.target!==input &&

        !suggestionBox.contains(event.target)

    ){

        hideSuggestions();

    }

});

document.addEventListener("DOMContentLoaded",()=>{

    const input =
        document.getElementById("query");

    if(!input) return;

    let timer=null;

    input.addEventListener("keyup",()=>{

        clearTimeout(timer);

        timer=setTimeout(async()=>{

            const query=input.value.trim();

            if(query.length<2){

                hideSuggestions();

                return;

            }

            const suggestions =
                await apiSuggestions(query);

            renderSuggestions(suggestions);

        },300);

    });

});