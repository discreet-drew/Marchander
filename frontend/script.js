async function searchProduct(){

    const query =
    document.getElementById(
        "query"
    ).value;

    document
    .getElementById(
        "loading"
    )
    .innerHTML =
    "Searching Flipkart...";

    const response =
    await fetch(
        "http://127.0.0.1:5000/search",
        {
            method:"POST",

            headers:{
                "Content-Type":
                "application/json"
            },

            body:JSON.stringify({
                query
            })
        }
    );

    const data =
    await response.json();

    document
    .getElementById(
        "loading"
    )
    .innerHTML = "";

    document
    .getElementById(
        "result"
    )
    .innerHTML =

    `
    <div class="card">

        <h2>
            ${data.title}
        </h2>

        <div class="price">

            &#8377;${data.price}

        </div>

        <p>

            Store:
            ${data.store}

        </p>

        <p>

            Currency:
            ${data.currency}

        </p>

    </div>
    `;
}