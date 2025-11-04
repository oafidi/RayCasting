<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%
    request.setCharacterEncoding("UTF-8");

    double qte1 = Double.parseDouble(request.getParameter("qte1"));
    double qte2 = Double.parseDouble(request.getParameter("qte2"));
    double qte3 = Double.parseDouble(request.getParameter("qte3"));
    double prix1 = Double.parseDouble(request.getParameter("prix1"));
    double prix2 = Double.parseDouble(request.getParameter("prix2"));
    double prix3 = Double.parseDouble(request.getParameter("prix3"));
    double remise = Double.parseDouble(request.getParameter("remise"));

    double totalHT1 = qte1 * prix1;
    double totalHT2 = qte2 * prix2;
    double totalHT3 = qte3 * prix3;
    double totalNetHT = totalHT1 + totalHT2 + totalHT3;
    double tva = totalNetHT * 0.20;
    double totalTTC = totalNetHT + tva - remise;
%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Facture Détails</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-dark text-white">
<div class="container mt-5 p-4 bg-secondary rounded shadow">
    <h3 class="text-center text-warning mb-4">Détails de la Facture</h3>

    <p><strong>Numéro :</strong> <%= request.getParameter("numFacture") %></p>
    <p><strong>Client :</strong> <%= request.getParameter("nomClient") %></p>
    <p><strong>Email :</strong> <%= request.getParameter("emailClient") %></p>

    <table class="table table-bordered table-dark">
        <thead>
            <tr>
                <th>Description</th>
                <th>Qté</th>
                <th>Prix Unitaire</th>
                <th>Total HT</th>
            </tr>
        </thead>
        <tbody>
            <tr><td>Macbook Pro M2</td><td><%= qte1 %></td><td><%= prix1 %></td><td><%= totalHT1 %></td></tr>
            <tr><td>Imprimante HP 7740</td><td><%= qte2 %></td><td><%= prix2 %></td><td><%= totalHT2 %></td></tr>
            <tr><td>Disque SSD 500GO</td><td><%= qte3 %></td><td><%= prix3 %></td><td><%= totalHT3 %></td></tr>
        </tbody>
    </table>

    <div class="text-end">
        <p><strong>Total net HT :</strong> <%= totalNetHT %> DH</p>
        <p><strong>TVA (20%) :</strong> <%= tva %> DH</p>
        <p><strong>Remise :</strong> <%= remise %> DH</p>
        <h5 class="text-warning">Total TTC : <%= totalTTC %> DH</h5>
    </div>
</div>
</body>
</html>
