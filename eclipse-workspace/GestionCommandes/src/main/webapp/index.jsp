<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
<%
    // Génération d’un numéro de facture aléatoire entre 1 et 1000
    int number = (int)(Math.random() * 1000) + 1;
    String value = "FA-" + number;
%>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulaire Facture Client</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #f8f9fa;
            padding: 30px;
        }
        .facture-header {
            margin-bottom: 20px;
        }
        .table thead {
            background-color: #3d8bcc;
            color: white;
        }
        .table tbody tr td:first-child {
            font-weight: 600;
            color: #2b4c2b;
        }
        .total-section {
            margin-top: 30px;
        }
        .total-box {
            border: 1px solid #dee2e6;
            padding: 10px;
            background-color: white;
        }
    </style>
</head>
<body>

<div class="container bg-white p-4 shadow rounded">
    <h3 class="text-center mb-4">Formulaire de Facture Client</h3>

    <form action="facture.jsp" method="post">

        <!-- Informations client -->
        <div class="row facture-header">
            <div class="col-md-4">
                <label class="form-label">Nom Client :</label>
                <input type="text" name="nomClient" class="form-control" required>
            </div>
            <div class="col-md-4">
                <label class="form-label">Adresse Client :</label>
                <input type="text" name="adresseClient" class="form-control" required>
            </div>
            <div class="col-md-4">
                <label class="form-label">Email Client :</label>
                <input type="email" name="emailClient" class="form-control" required>
            </div>
        </div>

        <!-- Numéro de facture -->
        <div class="d-flex justify-content-end mb-3">
            <div class="d-flex align-items-center">
                <label class="form-label me-2 mb-0">Facture N° :</label>
                <input type="text" name="numeroFacture" value="<%= value %>" class="form-control" style="width:150px;" readonly>
            </div>
        </div>

        <!-- Tableau des produits -->
        <table class="table table-bordered">
            <thead class="text-center">
                <tr>
                    <th>Description</th>
                    <th>Qté</th>
                    <th>Prix Unitaire</th>
                    <th>Total HT</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Ordinateur portable, Macbook Pro M2</td>
                    <td><input type="number" name="qte1" class="form-control" min="0"></td>
                    <td><input type="number" name="prix1" class="form-control" min="0" step="0.01"></td>
                    <td><input type="text" name="total1" class="form-control" readonly></td>
                </tr>
                <tr>
                    <td>Imprimante HP Pro 7740</td>
                    <td><input type="number" name="qte2" class="form-control" min="0"></td>
                    <td><input type="number" name="prix2" class="form-control" min="0" step="0.01"></td>
                    <td><input type="text" name="total2" class="form-control" readonly></td>
                </tr>
                <tr>
                    <td>Disque dur SSD 500GO</td>
                    <td><input type="number" name="qte3" class="form-control" min="0"></td>
                    <td><input type="number" name="prix3" class="form-control" min="0" step="0.01"></td>
                    <td><input type="text" name="total3" class="form-control" readonly></td>
                </tr>
            </tbody>
        </table>

        <!-- Conditions et Totaux -->
        <div class="row total-section">
            <div class="col-md-6">
                <h6 class="fw-bold">Conditions de paiement</h6>
                <p>
                    Les modes de paiement acceptés incluent le chèque, le virement bancaire
                    et la carte de crédit.
                </p>
            </div>
            <div class="col-md-6">
                <div class="total-box">
                    <div class="d-flex justify-content-between">
                        <span>Total net HT :</span>
                        <input type="text" name="totalHT" class="form-control text-end" style="width:120px;" readonly>
                    </div>
                    <div class="d-flex justify-content-between mt-2">
                        <span>TVA :</span>
                        <input type="number" name="tva" class="form-control text-end" style="width:120px;">
                    </div>
                    <div class="d-flex justify-content-between mt-2">
                        <span>Remise :</span>
                        <input type="number" name="remise" class="form-control text-end" style="width:120px;">
                    </div>
                    <hr>
                    <div class="d-flex justify-content-between fw-bold">
                        <span>Total TTC :</span>
                        <input type="text" name="totalTTC" class="form-control text-end" style="width:120px;" value="0.00 DH" readonly>
                    </div>
                </div>
            </div>
        </div>

        <!-- Boutons -->
        <div class="text-center mt-4">
            <button type="submit" class="btn btn-success px-4">Soumettre</button>
            <button type="reset" class="btn btn-secondary px-4">Annuler</button>
        </div>
    </form>
</div>

</body>
</html>
