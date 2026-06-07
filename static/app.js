const searchBtn = document.getElementById("searchBtn");
const resultsDiv = document.getElementById("results");

async function doSearch() {
  const query = document.getElementById("query").value;
  const maxPrice = document.getElementById("maxPrice").value;

  resultsDiv.innerHTML = '<p class="text-gray-600">Searching...</p>';

  const params = new URLSearchParams({ q: query, max_price: maxPrice });
  const response = await fetch("/api/search?" + params.toString());
  const deals = await response.json();

  if (deals.length === 0) {
    resultsDiv.innerHTML = '<p class="text-gray-600">No deals found.</p>';
    return;
  }

  resultsDiv.innerHTML = deals.map(function (deal) {
    return (
      '<a href="' + deal.url + '" target="_blank" class="block bg-white rounded-lg shadow hover:shadow-md overflow-hidden">' +
        '<img src="' + deal.image + '" alt="" class="w-full h-40 object-cover" />' +
        '<div class="p-3">' +
          '<p class="text-sm font-medium text-gray-800 line-clamp-2">' + deal.title + '</p>' +
          '<p class="text-lg font-bold text-green-600 mt-1">$' + deal.price + '</p>' +
          '<p class="text-xs text-gray-400 mt-1">' + deal.source + '</p>' +
        '</div>' +
      '</a>'
    );
  }).join("");
}

searchBtn.addEventListener("click", doSearch);