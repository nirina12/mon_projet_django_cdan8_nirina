$.ajax({
  url: "/datalistfihiranavoalohany/",
  type: "GET",
  dataType: "json",
  success: function (data) {
    var jsonData = JSON.parse(data);
    $("#tableContent").empty();
    var columnCount = 3; // Par défaut, 3 colonnes
    if ($(window).width() < 768) {
      // Pour les écrans plus petits que 768px, utiliser une seule colonne
      columnCount = 1;
    }

    $.each(jsonData, function (index, item) {
      // Accédez aux propriétés de chaque objet
      var hira = item.fields.Range_file + " " + item.fields.Titre;

      var columnClass =
        "col-lg-" + 12 / columnCount + " col-md-" + 12 / columnCount;
      if (index % columnCount === 0) {
        // Ajoute une classe pour la première colonne de chaque ligne
        columnClass += " col-lg-offset-0";
      }

      var column = "<div class='" + columnClass + "'>";
      column += "<div class='panel panel-default'>";
      
      column += "<div class='panel-body'><a href='/Mijery fihirana voalohany/" + item.fields.Range_file + "/'>" + hira + "</a></div>";
      column += "</div>";
      column += "</div>";

      // Ajouter la colonne au tableau
      $("#tableContent").append(column);
    });
    $("#tableContent").addClass("row");
  },
  error: function (xhr, status, error) {
    console.log("Erreur lors de la récupération des données");
  },
});

var contentFihiranaBeaderBtn = $("#contentFihirana_header_btn")

contentFihiranaBeaderBtn.click(function() {
    console.log("bonjour")
    $("#contentFihirana-header-option")
})


