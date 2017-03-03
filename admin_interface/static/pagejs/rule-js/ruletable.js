function format ( d ) {
    // `d` is the original data object for the row
    return '<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">'+
        '<tr>'+
            '<td>Full name:</td>'+
            '<td>'+d.name+'</td>'+
        '</tr>'+
        '<tr>'+
            '<td>Extension number:</td>'+
            '<td>'+d.extn+'</td>'+
        '</tr>'+
        '<tr>'+
            '<td>Extra info:</td>'+
            '<td>And any further details here (images etc)...</td>'+
        '</tr>'+
    '</table>';
}



$(document).ready(function() {
	var token = $('input[name="csrfmiddlewaretoken"]').prop('value');
	$.ajax({
              	type: 'POST',
              	dataType: 'json',
              	url: '/get_redis_rules/',
              	data: {
                        'csrfmiddlewaretoken': token
               	},
               	cache: false,
				success: function(data) {
				   	var json = [];
					for(var i =0; i < data.length;i++){
						var rule_str = data[i][0];
						var rule_arr = rule_str.split(':');
						json[i] = {
										"rule_name" : rule_arr[0],
                    					"status" : rule_arr[1],
                    					"mode" : rule_arr[2],
                    					"break_on_match" : rule_arr[3],
                    					"key_strategy" : rule_arr[4],
                    					"rc_autodetect" : rule_arr[5],
                    					"default_rc" : rule_arr[6],
                    					"reason_code" : rule_arr[7],
                    					"ttl" : rule_arr[8],
                    					"conditions" : []
                		};
						var cond = rule_arr[rule_arr.length-1].split('&');
						cond.forEach(function(condition,index,arr) {
								var cond_replace,cond_parse,cond_type,cond_final;
								cond_replace = condition.replace(/[\)\(\{\}]/g,'');
    							cond_parse = cond_replace.split('|');
								cond_type = cond_parse[1];
   								cond_parse.splice(1,1);//remove type from cond
								if(cond_parse.length === 3) {
    								cond_final = cond_parse.join(' ');    
        							json[i].conditions.push(cond_final);
								}
								else if(cond_parse.length === 4) {
    								cond_parse.splice(2,1,cond_parse[2]+'%');
    								cond_final = cond_parse.join(' ');
        							json[i].conditions.push(cond_final);
     
    							}
						});

					   
					}
				
                   	render_rules(json);
               },
               error: function(data) {
				   
                        console.log('ERROR');
              }
        });
	function render_rules(data){
    var table = $('#rule-table').DataTable( {
        "aaData": data,
		
        "aoColumns": [
            
            { "mData": "rule_name" },
			/*{ "mData": "mode",
			  render: function ( data, type, row ) {
                    if ( row.mode == 0 ) {
                        return '<i class="fa fa-circle" aria-hidden="true" style="color:#fea444;"></i>';
                    }
				    else if(row.mode == 1) {
						return '<i class="fa fa-circle" aria-hidden="true" style="color:#84ba24;"></i>';
                    }
                   
              },
			},*/
			{
                "mData":   "status",
                render: function ( data, type, row ) {
                    if (row.status == 0 && row.mode == 0) { //disabled and monitor mode red  
                        return '<i class="fa fa-circle" aria-hidden="true" style="color:#ee2f2f;"></i>';
                    }
					else if(row.status == 1 && row.mode == 1) { // enabled and active mode green  
						return '<i class="fa fa-circle" aria-hidden="true" style="color:#84ba24;"></i>';
                    }
					else if(row.status == 1 && row.mode == 0) { // enabled and monitor mode amber  
						return '<i class="fa fa-circle" aria-hidden="true" style="color:#fea444;"></i>';
                    }
                    
                },
                
            },
            { "mData": null,
			  "className": "dt-left",
              "mRender": function (data, type, row) {
				  		var data='<code style ="color: white;background-color: #87cefa">'+row.conditions[0]+'</code>&nbsp';
				  		for(var i=1;i<row.conditions.length;i++){
							data += '<code style ="color: white;background-color: #87cefa">'+row.conditions[i]+'</code>&nbsp';
          
						}
				  		return data;
                    },
			},
			{
                "mdata": null,
                defaultContent: '<a id ="trigger" href="#"><i class="fa fa-pencil-square-o" aria-hidden="true"></i></a>'
				//"defaultContent": "<button>Click!</button>"
            }
           
        ],
		 "columnDefs": [
			{"className": "dt-center", "targets": "_all"}
         ],
        "ordering": false,
		"paging": false,
		"scrollY": "300px",
        "scrollCollapse": true
		

    } );
	
	$('#rule-table').on( 'click', '#trigger', function () {
        var data = table.row( $(this).parents('tr') ).data();
		    $("#editModal").modal("show");
        	$("#rule-name").val(data.rule_name);
			if(data.status == 1){
				$("#status").prop("checked",true);
			}
			else{
				$("#status").prop("checked",false);
			}
			if(data.mode ==1){
				$("#mode").prop("checked",true);
			}
			else{
				$("#mode").prop("checked",false);
			}
			if(data.break_on_match == 1){
				$("#brk_on_m").prop("checked",true);
			}
			else{
				$("#brk_on_m").prop("checked",false);
			}
			if(data.rc_autodetect == 1){
				$("#rc_auto").prop("checked",true);
			}
			else{
				$("#rc_auto").prop("checked",false);
			}
			$("#key-strategy").val(data.key_strategy).change();
			$("#response-code").val(data.default_rc).change();
			$("#reason-code").val(data.reason_code);
			$("#ttl").val(data.ttl);
			console.log(data.mode+"---------"+data.conditions);
		
    } );
	/*$('#editModal').modal({
        keyboard: true,
        backdrop: "static",
        show:false,
        
    }).on('show', function(){
		console.log($(this).closest('table tbody tr td').children()[0].textContent);
        $("#txtfname").val($(this).closest('table tbody tr td').children()[0].textContent);
        //make your ajax call populate items or what even you need
     });*/
	}
} );