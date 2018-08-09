/*
* dbreport-table-template - v1.0.0 - 2018-02-07
* 巡检报告表格模版，用于生成最终的dbreport-table.js文件
*
* Copyright (c) 2018 duchengwen
* mail: duchengwen@gmail.com
* QQ:   23828728
* 微信: 18047120719
* 
*********************************************************************************************
** Version | Complete Time    | Description                                                **
**---------|------------------|------------------------------------------------------------**
**     1.0 | 2018-02-07 17:50 | First Edition                                              **
*********************************************************************************************
*/

var TableInit = function (tableID, columnDefine, tableDataValue) {
	var oTableInit = new Object();
	
	//初始化Table
	oTableInit.Init = function () {
		$('#' + tableID).bootstrapTable({
		toolbar: '#toolbar',                //工具按钮用哪个容器
		striped: true,                      //是否显示行间隔色
		cache: false,                       //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
		pagination: true,                   //是否显示分页（*）
		sortable: true,                     //是否启用排序
		sortOrder: "asc",                   //排序方式
		//queryParams: oTableInit.queryParams,//传递参数
		//sidePagination: "server",           //分页方式：client客户端分页，server服务端分页（*）
		pageNumber:1,                       //初始化加载第一页，默认第一页
		pageSize: 10,                       //每页的记录行数（*）
		pageList: [10, 25, 50, 100],        //可供选择的每页的行数（*）
		search: true,                       //是否显示表格搜索，此搜索是客户端搜索，不会进服务端
		showExport: true,
		exportDataType: 'basic',              //basic', 'all', 'selected'.
		exportTypes: ['json', 'xml', 'csv', 'txt', 'sql', 'excel'],  //导出文件类型  
		showToggle:true,                    //是否显示详细视图和列表视图的切换按钮
		cardView: false,                    //是否显示详细视图
		detailView: false,                  //是否显示父子表
		columns: columnDefine,
		data: tableDataValue,
		});
	};

	return oTableInit;
};