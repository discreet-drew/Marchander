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