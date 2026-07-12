console.log("api.js loaded");
const API_BASE_URL = "http://127.0.0.1:5000";

async function getRequest(endpoint) {
    const response = await fetch(`${API_BASE_URL}${endpoint}`);

    if (!response.ok) {
        throw new Error(
            `GET ${endpoint} failed (${response.status})`
        );
    }

    return await response.json();
}

async function postRequest(endpoint, body) {

    const response = await fetch(
        `${API_BASE_URL}${endpoint}`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(body)
        }
    );

    if (!response.ok) {
        let message = "Server Error";
        try {
            const err = await response.json();

            message = err.error || message;

        }
        catch {
            message = response.statusText;
        }
        throw new Error(message);
    }
    return await response.json();
}

async function apiSearch(query) {

    return await postRequest(
        "/search",
        {
            query: query
        }
    );
}

async function apiHistory(product) {

    return await getRequest(

        `/history/${encodeURIComponent(product)}`

    );
}

async function apiRecommendations(query) {

    try {

        return await getRequest(

            `/recommend?query=${encodeURIComponent(query)}`

        );

    }

    catch (error) {

        console.warn(

            "Recommendation API:",

            error.message

        );

        return [];
    }
}

async function apiSuggestions(query) {

    try {

        return await getRequest(

            `/suggest?q=${encodeURIComponent(query)}`

        );

    }

    catch (error) {

        console.warn(

            "Suggestion API:",

            error.message

        );

        return [];
    }
}

async function apiCreateAlert(

    email,

    product,

    targetPrice

) {

    return await postRequest(

        "/alerts",

        {

            email: email,

            product: product,

            target_price: targetPrice

        }

    );

}

async function apiAlerts() {

    return await getRequest(

        "/alerts"

    );

}

async function apiDeleteAlert(id) {

    const response = await fetch(

        `${API_BASE_URL}/alerts/${id}`,

        {

            method: "DELETE"

        }

    );

    if (!response.ok) {

        throw new Error(

            "Unable to delete alert"

        );

    }
    return await response.json();

}

async function apiHealth() {

    try {

        return await getRequest("/");

    }

    catch {

        return {

            status: "offline"

        };

    }

}