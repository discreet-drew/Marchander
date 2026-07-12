/*****************************************************************
 * Marchander
 * Main Controller
 *****************************************************************/

console.log("script.js loaded");

/******************************************************
 * Loading Animation
 ******************************************************/

let loadingTimer = null;

const loadingMessages = [

    "Searching Flipkart...",

    "Searching Amazon...",

    "Comparing Prices...",

    "Finding Best Deal...",

    "Loading Analytics..."

];

function startLoading(){

    const loading = document.getElementById("loading");

    let index = 0;

    loading.innerHTML = loadingMessages[0];

    loadingTimer = setInterval(()=>{

        index++;

        if(index >= loadingMessages.length){

            index = 0;

        }

        loading.innerHTML = loadingMessages[index];

    },800);

}

function stopLoading(){

    clearInterval(loadingTimer);

    document.getElementById("loading").innerHTML="";

}


/******************************************************
 * Search Product
 ******************************************************/

async function searchProduct(){

    const query = document

        .getElementById("query")

        .value

        .trim();

    if(query===""){

        alert("Please enter a product.");

        return;

    }

    startLoading();

    try{

        //------------------------------------------------
        // API Calls
        //------------------------------------------------

        const comparison = await apiSearch(query);

        const analytics = await apiHistory(query);

        const recommendations = await apiRecommendations(query);

        //------------------------------------------------
        // Render UI
        //------------------------------------------------

        renderComparison(comparison);

        renderAnalytics(analytics);

        renderRecommendations(recommendations);

    }

    catch(error){

        console.error(error);

        document.getElementById("result").innerHTML =

        `

        <div class="card">

            <h2>Error</h2>

            <p>${error.message}</p>

        </div>

        `;

    }

    finally{

        stopLoading();

    }

}

async function showSuggestions(){

    const query = document

        .getElementById("query")

        .value

        .trim();

    if(query.length<2){

        document

        .getElementById("suggestions")

        .innerHTML="";

        return;

    }

    const suggestions =

        await apiSuggestions(query);

    renderSuggestions(suggestions);

}

function fillSearch(product){

    document

        .getElementById("query")

        .value = product;

    document

        .getElementById("suggestions")

        .innerHTML = "";

}

async function createAlert(){

    const email =

        document

        .getElementById("email")

        .value;

    const targetPrice =

        document

        .getElementById("targetPrice")

        .value;

    const product =

        document

        .getElementById("query")

        .value;

    if(

        email===""

        ||

        targetPrice===""

        ||

        product===""

    ){

        alert(

            "Please complete all fields."

        );

        return;

    }

    try{

        await apiCreateAlert(

            email,

            product,

            targetPrice

        );

        alert(

            "Price Alert Created Successfully!"

        );

    }

    catch(error){

        alert(

            error.message

        );

    }

}

function showElectronics(){

    document

        .querySelector(".hero h1")

        .innerHTML =

        "Marchander Electronics";

}

function showFashion(){

    document

        .querySelector(".hero h1")

        .innerHTML =

        "Marchander Fashion";

}

document

.getElementById("query")

.addEventListener(

    "keypress",

    function(event){

        if(event.key==="Enter"){

            searchProduct();

        }

    }

);

window.onload = async function(){

    try{

        const health = await apiHealth();

        console.log(

            "Backend:",

            health

        );

    }

    catch{

        console.log(

            "Backend Offline"

        );

    }

};