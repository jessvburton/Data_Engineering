function exportAndModifySheetsWithoutAlteringOriginals() {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
 
  // Define columns to delete for each sheet by sheet name
  var columnsToDeleteMap = {
    "SHEET_NAME1": [], // Replace "SHEET_NAME1" with the sheet name you want to export and followed by the columns you want to delete
    "SHEET_NAME2": [], // Repeat as necessary 
  };
 
 
  for (var sheetName in columnsToDeleteMap) {
    var originalSheet = spreadsheet.getSheetByName(sheetName);
   
    if (originalSheet !== null) {
      // Create a temporary copy of the original sheet
      var temporarySheet = originalSheet.copyTo(spreadsheet);
      temporarySheet.setName(sheetName + "_Temp");
     
      var columnsToDelete = columnsToDeleteMap[sheetName];
     
      // Delete specified columns for the temporary sheet
      columnsToDelete.sort(function(a, b){ return b - a; }); // Sort in descending order to avoid issues with column deletion
      columnsToDelete.forEach(function(colIndex) {
        temporarySheet.deleteColumn(colIndex + 1); // Adding 1 because deleteColumn() uses 1-indexed columns
      });
     
      // Export modified data of the temporary sheet to CSV
      var dataRange = temporarySheet.getDataRange();
      var csv = "";
      var values = dataRange.getDisplayValues();
     
      for (var i = 0; i < values.length; i++) {
        var row = values[i];
        for (var j = 0; j < row.length; j++) {
          csv += '"' + row[j] + '",';
        }
        csv += "\n";
      }

      var dateTime = Utilities.formatDate(new Date(), "GMT", "yyyyMMdd'_'HHmmss");
	    var date = Utilities.formatDate(new Date(), "GMT", "yyyyMMdd");

      // Need to add code here to check if date/target folder exists, if not create it once
      const rootFolder = DriveApp.getFolderById('YOUR_FOLDER_ID'); // Replace 'YOUR_FOLDER_ID' with the ID of the folder where you want to save the CSV
      const targetFolderName = date;
  
      // Get folders by name
      const folderIterator = rootFolder.getFoldersByName(targetFolderName);

      let targetFolder;
      if (folderIterator.hasNext()) {
        // When the folder exists
        targetFolder = folderIterator.next();
      } else {
        // When the folder doesn't exist
        targetFolder = rootFolder.createFolder(targetFolderName);
      }

      var file = targetFolder.createFile(dateTime + "_" + sheetName + ".csv", csv, MimeType.CSV);
     
      // Delete the temporary sheet after exporting
      spreadsheet.deleteSheet(temporarySheet);
    } else {
      Logger.log("Sheet '" + sheetName + "' not found.");
    }
  }
}
