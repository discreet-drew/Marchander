async function searchProduct() {

    const query =
        document.getElementById(
            "query"
        ).value;

    document
        .getElementById(
            "loading"
        )
        .innerHTML =
        "Searching stores...";

    document
        .getElementById(
            "result"
        )
        .innerHTML = "";

    try {

        const response =
            await fetch(
                "http://127.0.0.1:5000/search",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        query
                    })
                }
            );

        const data =
            await response.json();

        const historyResponse = await fetch
        (
        `http://127.0.0.1:5000/history/${query}`
        );
        const analytics = await historyResponse.json();
        console.log(data);

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
            <div class="results">

                <div class="card">

                    <h2>Flipkart</h2>

                    <div class="price">

                        ₹${data.flipkart?.price || "N/A"}

                    </div>

                </div>

                <div class="card">

                    <h2>Amazon</h2>

                    <div class="price">

                        ₹${data.amazon?.price || "N/A"}

                    </div>

                </div>

            </div>

            <div class="best-price">

                <div class="badge">

                    BEST DEAL

                </div>

                <h2>

                    Lowest Price Available At

                </h2>

                <div class="winner">

                    ${data.best_store || "Unavailable"}

                </div>

                <div class="price">

                    ${
                        data.lowest_price
                        ? `₹${data.lowest_price}`
                        : "N/A"
                    }

                </div>

            </div>
            `;

         document.getElementById(

            "stats"

            ).innerHTML =

            `

            <div class="stat-card">

            <h3>Current</h3>

            <p>₹${analytics.current_price}</p>

            </div>

            <div class="stat-card">

            <h3>Lowest</h3>

            <p>₹${analytics.lowest_price}</p>

            </div>

            <div class="stat-card">

            <h3>Highest</h3>

            <p>₹${analytics.highest_price}</p>

            </div>

            <div class="stat-card">

            <h3>Average</h3>

            <p>₹${analytics.average_price}</p>

            </div>

            `;

        const labels = analytics.history.map(

        item=>item.date

        );

        const prices = analytics.history.map(

        item=>item.price

        );

        const ctx = document

        .getElementById(

        "priceChart"

        )

        .getContext("2d");

        new Chart(

        ctx,

        {

        type:"line",

        data:{

        labels,

        datasets:[

        {

        label:"Price",

        data:prices,

        fill:false,

        tension:0.4

        }

        ]

        }

        }

     ); 
    }   

catch(error){

        console.error(error);

        document
            .getElementById(
                "loading"
            )
            .innerHTML =

            "Something went wrong.";
    }
}