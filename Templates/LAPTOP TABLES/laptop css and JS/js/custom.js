// =============  Data Table - (Start) ================= //

$(document).ready(function(){
    
    var table = $('#example').DataTable({
        
        buttons:['copy', 'csv', 'excel', 'pdf', 'print','Add Laptop']
        
    });
    
    
    table.buttons().container()
    .appendTo('#example_wrapper .col-md-6:eq(0)');

});

// =============  Data Table - (End) ================= //
