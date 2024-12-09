

async function sortQuery() {
    const vals = document.getElementById("inputBox").value.split(",").map(Number);
    console.log(vals);

    const response = await fetch("http://192.168.1.175:1234/sort", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: vals
    });

    const data = await response.json();  
    document.getElementById("sortedList").innerText = data.sorted_vals.join(", "); 

}