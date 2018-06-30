package com.maxsoft.intelliapi.util.reader;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

import com.maxsoft.intelliapi.api.Base;
import com.maxsoft.intelliapi.util.fileoperator.Excel;
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.testng.Assert;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;


public abstract class ApiDocument {

	private static Base baseObj = new Base();
	private static String value = "";
	private static String error = "";
	private static int sheetName = 0;

	public static String getDataFromExcel(int row, int column) {
		try {
			FileInputStream excelFile = new FileInputStream(new File(baseObj.getAPIDocumentFilePath()));
			System.out.println(baseObj.getAPIDocumentFilePath());
			Workbook workbook = new XSSFWorkbook(excelFile);
			Sheet workSheet = workbook.getSheetAt(sheetName);
			value = workSheet.getRow(row).getCell(column).getStringCellValue();
			System.out.println(value);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return value;
	}

	public static String getAPIEndpoint(String apiEndpointName) throws IOException {
		int row, column;
		row = Excel.findRowNumber(apiEndpointName);
		column = Excel.findColumnNumber(apiEndpointName) + 1;
		error = "\""+ apiEndpointName + "\" API Endpoint Name is not exist in the API Document Excel file located in \"" + baseObj.getAPIDocumentFilePath() + "\"";
		if (row == 0 && column == 1){
			Assert.fail(error);
			return error;
		} else {
			return getDataFromExcel(row, column);
		}
	}

	public static String getHttpMethod(String apiEndpointName) throws IOException {
		int row, column;
		row = Excel.findRowNumber(apiEndpointName);
		column = Excel.findColumnNumber(apiEndpointName) + 2;
		error = "\""+ apiEndpointName + "\" API Endpoint Name is not exist in the API Document Excel file located in \"" + baseObj.getAPIDocumentFilePath() + "\"";
		if (row == 0 && column == 2){
			Assert.fail(error);
			return error;
		} else {
			return getDataFromExcel(row, column);
		}
	}

	public static String getBodyType(String apiEndpointName) throws IOException {
		int row, column;
		row = Excel.findRowNumber(apiEndpointName);
		column = Excel.findColumnNumber(apiEndpointName) + 3;
		error = "\""+ apiEndpointName + "\" API Endpoint Name is not exist in the API Document Excel file located in \"" + baseObj.getAPIDocumentFilePath() + "\"";
		if (row == 0 && column == 2){
			Assert.fail(error);
			return error;
		} else {
			return getDataFromExcel(row, column);
		}
	}

	public static String getRequestPayloadTemplate(String apiEndpointName) throws IOException {
		int row, column;
		row = Excel.findRowNumber(apiEndpointName);
		column = Excel.findColumnNumber(apiEndpointName) + 4;
		error = "\""+ apiEndpointName + "\" API Endpoint Name is not exist in the API Document Excel file located in \"" + baseObj.getAPIDocumentFilePath() + "\"";
		if (row == 0 && column == 2){
			Assert.fail(error);
			return error;
		} else {
			return getDataFromExcel(row, column);
		}
	}


}