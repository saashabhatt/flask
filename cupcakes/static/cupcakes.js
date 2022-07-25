const URL = "http://localhost:5000/api";

function generateHTML(cupcake) {
    return `<div>
                <li id="${cupcake.id}">${cupcake.flavor}, ${cupcake.size}, ${cupcake.rating}
                <button class="delete">X</button></li>
                <img src="${cupcake.image}" height=250px width=250px></img>
            </div>`;
}

async function displaycupcakes() {
    const response = await axios.get(`${URL}/cupcakes`);

    for (let item of response.data.cupcakes) {
        newcupcake = $(generateHTML(item));
        $("#list-cupcakes").append(newcupcake);
    }
}

$("#cupcakeform").on("submit", async function(evt) {
    evt.preventDefault();

    let flavor = $("#flavor").val();
    let size = $("#size").val();
    let rating = $("#Rating").val();
    let image = $("#img_url").val();

    const newresponse = await axios.post(`${URL}/cupcakes`, {
        flavor,
        rating,
        size,
        image
    });
    let newcake = $(generateHTML(newresponse.data.cupcakes));
    $("#list-cupcakes").append(newcake);
    $("#cupcakeform").trigger("reset");
});

$("#list-cupcakes").on("click",".delete", async function(evt) {
    evt.preventDefault();
    let $cupcake = $(evt.target).closest("li");
    let cupcakeid = $cupcake.attr("id");

    await axios.delete(`${URL}/cupcakes/${cupcakeid}`);
    $cupcake.closest('div').remove();
})

$(displaycupcakes);
