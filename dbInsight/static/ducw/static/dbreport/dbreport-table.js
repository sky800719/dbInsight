/**
 * 记录数少的查询结果表格
 */
var miniTableInit = function(tableID, columnDefine, tableDataValue) {
  var oTableInit = new Object();

  // 初始化Table
  oTableInit.Init = function() {
    $('#' + tableID).bootstrapTable({
      toolbar : '#toolbar', // 工具按钮用哪个容器
      striped : true, // 是否显示行间隔色
      cache : false, // 是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
      pageNumber : 1, // 初始化加载第一页，默认第一页
      columns : columnDefine,
      data : tableDataValue,
    });
  };

  return oTableInit;
};

/**
 * 记录数多的查询结果表格，提供导出，查询等功能
 */
var hugeTableInit = function(tableID, columnDefine, tableDataValue) {
  var oTableInit = new Object();

  // 初始化Table
  oTableInit.Init = function() {
    $('#' + tableID).bootstrapTable({
      toolbar : '#toolbar', // 工具按钮用哪个容器
      striped : true, // 是否显示行间隔色
      cache : false, // 是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
      pagination : true, // 是否显示分页（*）
      sortable : true, // 是否启用排序
      sortOrder : "asc", // 排序方式
      pageNumber : 1, // 初始化加载第一页，默认第一页
      pageSize : 10, // 每页的记录行数（*）
      pageList : [ 10, 50, 100 ], // 可供选择的每页的行数（*）
      search : true, // 是否显示表格搜索，此搜索是客户端搜索，不会进服务端
      showExport : true,
      exportDataType : 'basic', // basic', 'all', 'selected'.
      exportTypes : [ 'json', 'xml', 'csv', 'txt', 'sql', 'excel' ], // 导出文件类型
      showToggle : true, // 是否显示详细视图和列表视图的切换按钮
      cardView : false, // 是否显示详细视图
      detailView : false, // 是否显示父子表
      columns : columnDefine,
      data : tableDataValue,
    });
  };

  return oTableInit;
};

/**
 * 菜单点击处理事件，用于解决当菜单内容太多时，造成左侧菜单树无法完全展现的问题
 * @param menu
 * @returns
 */
function menuEvent(menu) 
{
  $("li").removeClass();
  $(menu).addClass("active");
}

/**
 * 初始化页面展现表格
 * @returns
 */
function reportTableInit() {
  var STORAGE_TABLESPACE_TAB = new hugeTableInit('INSTANCE_TABID2', INSTANCE_COLUMNVALUE, INSTANCE_DATAVALUE);
  STORAGE_TABLESPACE_TAB.Init();
}
