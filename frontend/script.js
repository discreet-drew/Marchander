let priceChart = null;
let loadingTimer = null;

const API = "http://127.0.0.1:5000";

async function apiSearch(query){
    const r = await fetch(`${API}/search`,{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({query})
    });
    if(!r.ok) throw new Error("Search API failed");
    return await r.json();
}

async function apiHistory(query){
    const r = await fetch(`${API}/history/${encodeURIComponent(query)}`);
    if(!r.ok) throw new Error("History API failed");
    return await r.json();
}

async function apiRecommendations(query){
    try{
        const r = await fetch(`${API}/recommend?query=${encodeURIComponent(query)}`);
        if(!r.ok) return [];
        return await r.json();
    }catch{
        return [];
    }
}

async function apiSuggestions(query){
    try{
        const r = await fetch(`${API}/suggest?q=${encodeURIComponent(query)}`);
        if(!r.ok) return [];
        return await r.json();
    }catch{
        return [];
    }
}



function money(v){
    if(v==null) return "N/A";
    return "₹"+Number(v).toLocaleString("en-IN");
}

function fillSearch(v){
    document.getElementById("query").value=v;
    document.getElementById("suggestions").innerHTML="";
}

const msgs=[
"Searching Flipkart...",
"Searching Amazon...",
"Matching Products...",
"Calculating Best Deal..."
];

function startLoading(){
    const div=document.getElementById("loading");
    let i=0;
    div.innerHTML=msgs[0];
    loadingTimer=setInterval(()=>{
        i=(i+1)%msgs.length;
        div.innerHTML=msgs[i];
    },900);
}

function stopLoading(){
    clearInterval(loadingTimer);
    document.getElementById("loading").innerHTML="";
}



async function showSuggestions(){

    const q=document.getElementById("query").value.trim();

    if(q.length<2){
        document.getElementById("suggestions").innerHTML="";
        return;
    }

    const suggestions=await apiSuggestions(q);

    document.getElementById("suggestions").innerHTML=
        suggestions.map(s=>
        `<div class="suggestion" onclick="fillSearch('${typeof s==="string"?s:s.product}')">
            ${typeof s==="string"?s:s.product}
        </div>`).join("");
}



function card(product){

    if(!product){
        return `<div class="card">
        <h2>Unavailable</h2>
        <div class="price">N/A</div></div>`;
    }

    return `
    <div class="card">

        <h2>${product.store}</h2>

        <div class="price">${money(product.price)}</div>

        <p>${product.title||""}</p>

        <p>${product.availability||"Available"}</p>

        ${product.url?`<a class="buy-btn" target="_blank" href="${product.url}">View Product</a>`:""}

    </div>`;
}

function renderComparison(data){

    document.getElementById("result").innerHTML=
    `<div class="results">
        ${card(data.flipkart)}
        ${card(data.amazon)}
    </div>`;

    document.getElementById("best-deal").innerHTML=
    `<div class="best-price">
        <div class="badge">BEST DEAL</div>
        <h2>${data.best_store||"Unavailable"}</h2>
        <div class="winner">${money(data.lowest_price)}</div>
        ${data.savings?`<div class="savings">You Save ${money(data.savings)}</div>`:""}
    </div>`;
}

function renderAnalytics(a){

document.getElementById("stats").innerHTML=
`
<div class="stat-card"><h3>Current</h3><p>${money(a.current_price)}</p></div>
<div class="stat-card"><h3>Lowest</h3><p>${money(a.lowest_price)}</p></div>
<div class="stat-card"><h3>Highest</h3><p>${money(a.highest_price)}</p></div>
<div class="stat-card"><h3>Average</h3><p>${money(a.average_price)}</p></div>
`;

const ctx=document.getElementById("priceChart").getContext("2d");

if(priceChart) priceChart.destroy();

priceChart=new Chart(ctx,{
type:"line",
data:{
labels:a.history.map(x=>x.date),
datasets:[{
label:"Price",
data:a.history.map(x=>x.price),
fill:true,
tension:.35
}]
},
options:{responsive:true,maintainAspectRatio:false}
});

}

function renderRecommendations(list){

const div=document.getElementById("recommendations");

if(!list.length){
div.innerHTML="<div class='recommendation-card'>No recommendations available.</div>";
return;
}

div.innerHTML=list.map(r=>`
<div class="recommendation-card">
<h3>${r.product??r}</h3>
${r.score?`<p>Similarity: ${(r.score*100).toFixed(1)}%</p>`:""}
</div>`).join("");

}



async function searchProduct(){

const q=document.getElementById("query").value.trim();

if(!q){
alert("Enter a product");
return;
}

startLoading();

try{

const result=await apiSearch(q);
const analytics=await apiHistory(q);
const recs=await apiRecommendations(q);

renderComparison(result);
renderAnalytics(analytics);
renderRecommendations(recs);

stopLoading();

}catch(e){

stopLoading();

console.error(e); 
console.log("Query:",query);

document.getElementById("result").innerHTML=
`<div class="card"><h2>Error</h2><p>${e.message}</p></div>`;

}

}



async function createAlert(){

const email=document.getElementById("email").value;
const price=document.getElementById("targetPrice").value;
const query=document.getElementById("query").value;

alert(`Alert feature backend endpoint to be connected.\n${email}\n${query}\n${price}`);

}



function showElectronics(){
document.querySelector(".hero h1").innerText="Marchander Electronics";
}

function showFashion(){
document.querySelector(".hero h1").innerText="Marchander Fashion";
}
