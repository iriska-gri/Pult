var FSO = new ActiveXObject("Scripting.FileSystemObject");
var Excel = new ActiveXObject("Excel.Application");
var ExSheet;

var Codes = new Array(
"49.3",
"49.4",
"51.1",
"51.21",
"52.23.1",
"52.23.11",
"52.23.12",
"52.23.13",
"52.23.19",
"55.1",
"55.10",
"55.11",
"55.12",
"55.2",
"55.20",
"55.23.3",
"55.30",
"55.40",
"55.51",
"55.52",
"55.90",
"56.1",
"56.10",
"56.10.1",
"56.10.2",
"56.10.21",
"56.10.22",
"56.10.23",
"56.10.24",
"56.10.3",
"56.21",
"56.29",
"56.29.1",
"56.29.2",
"56.29.3",
"56.29.4",
"56.3",
"56.30",
"79",
"79.1",
"79.11",
"79.12",
"79.90",
"79.90.1",
"79.90.2",
"79.90.21",
"79.90.22",
"79.90.3",
"79.90.31",
"79.90.32",
"85.41",
"86.90.4",
"88.91",
"90.0",
"90.01",
"90.02",
"90.03",
"90.04",
"90.04.1",
"90.04.2",
"90.04.3",
"93",
"93.01",
"93.02",
"93.03",
"93.04",
"93.05",
"93.1",
"93.11",
"93.12",
"93.13",
"93.19",
"93.2",
"93.21",
"93.29",
"93.29.1",
"93.29.2",
"93.29.3",
"93.29.9",
"95.1",
"95.11",
"95.12",
"95.2",
"95.21",
"95.22",
"95.22.1",
"95.22.2",
"95.23",
"95.24",
"95.24.1",
"95.24.2",
"95.25",
"95.25.1",
"95.25.2",
"95.29",
"95.29.1",
"95.29.11",
"95.29.12",
"95.29.2",
"95.29.4",
"95.29.41",
"95.29.42",
"95.29.43",
"95.29.6",
"95.29.7",
"95.29.9",
"96.01",
"96.02",
"96.04",
"»ÚÓ„Ó"
);

function DeleteCodes()
{
	RowCount = ExSheet.ActiveSheet.UsedRange.Rows.Count;
	StartRow = 6;
	Matched = false;

	for(i=StartRow; i<RowCount+1; i++)
	{
		Matched = false;
		CellValue = ExSheet.ActiveSheet.Cells(i, 1).Value;

		for(k=0; k<Codes.length; k++)
		{
			if(CellValue == Codes[k])
				Matched = true;
		}

		if(!Matched)
		{
			ExSheet.ActiveSheet.Rows(i).Delete();
			RowCount--;
			i--;
		}
	}
	
}

function AddSummColumns()
{
	ExSheet.ActiveSheet.Columns(2).Insert;
	ExSheet.ActiveSheet.Cells(5, 2).Value = "–‘-‚ÒÂ";
	ExSheet.ActiveSheet.Columns(2).columnWidth = 25;

	ExSheet.ActiveSheet.Columns(3).Insert;
	ExSheet.ActiveSheet.Cells(5, 3).Value = "–‘-Ã—œ";
	ExSheet.ActiveSheet.Columns(3).columnWidth = 25;

	RowCount = ExSheet.ActiveSheet.UsedRange.Rows.Count;
	StartRow = 6;
	for(i=StartRow; i<RowCount+1; i++)
	{
		ExSheet.ActiveSheet.Cells(i, 2).FormulaLocal = "=—”ÃÃ(D"+i+":CK"+i+")";
		ExSheet.ActiveSheet.Cells(i, 3).FormulaLocal = "=—”ÃÃ(CL"+i+":FS"+i+")";
	}

	ExSheet.ActiveSheet.Rows(RowCount).Insert;
}

function DeleteSheets()
{
	ExSheet.Application.DisplayAlerts = false;
	ExSheet.Sheets(4).Delete();
	ExSheet.Sheets(3).Delete();
	ExSheet.Sheets(2).Delete();
}

function ComplexCodes(aCode)
{
	RowCount = ExSheet.ActiveSheet.UsedRange.Rows.Count;
	ColCount = ExSheet.ActiveSheet.UsedRange.Columns.Count;
	StartRow = 6;
	CodeFirstRow = 0;
	CodeRowCount = 0;

	for(i=StartRow; i<RowCount; i++)
	{
		CellValue = ExSheet.ActiveSheet.Cells(i, 1).Text;
		if(CellValue.substr(0, 2) == aCode)
		{
			if(CodeFirstRow == 0)
				CodeFirstRow = i;
			CodeRowCount++;
		}
	}

	ExSheet.ActiveSheet.Rows(CodeFirstRow).Insert;
	ExSheet.ActiveSheet.Cells(CodeFirstRow, 1).Value = aCode;

	ExSheet.Application.ReferenceStyle = -4150;
	RowFrom  = CodeFirstRow + 1;
	RowTo = CodeFirstRow + CodeRowCount;
	for(k=2; k<ColCount; k++)
	{
		ExSheet.ActiveSheet.Cells(CodeFirstRow, k).FormulaLocal = "=—”ÃÃ(R" + RowFrom + "C" + k + ":R" + RowTo + "C" + k + ")";
		ExSheet.ActiveSheet.Cells(CodeFirstRow, k) = ExSheet.ActiveSheet.Cells(CodeFirstRow, k).Value;
	}
	ExSheet.Application.ReferenceStyle = 1;

	for(i=0; i<CodeRowCount; i++)
		ExSheet.ActiveSheet.Rows(CodeFirstRow+1).Delete;

	ExSheet.ActiveSheet.Columns(1).HorizontalAlignment = -4108;
}

function GetPath()
{
	F = FSO.GetFile(WScript.ScriptFullName)
	return FSO.GetParentFolderName(F);
}

function GetFileName()
{
	FileName = "";
	Folder = FSO.GetFolder(GetPath());
	fc = new Enumerator(Folder.files);
	for(; !fc.atEnd(); fc.moveNext())
	{
		if (fc.item().Name.substr(0, 11) == "ŒÚ˜ÂÚ Œ ¬›ƒ")
			FileName =  fc.item().Name;
	}
	return FileName;
}

function NewFileName()
{
	OrginalName = GetFileName();
	NewName = OrginalName.substr(0, 5) + "2" + OrginalName.substr(5, OrginalName.length - 5);
	return NewName;
}

// =======   Main   =======

FSO.CopyFile(GetFileName(), NewFileName());
ExSheet = Excel.Workbooks.Open(GetPath()+"\\"+NewFileName());
ExSheet.Application.Visible = false;

DeleteSheets();
DeleteCodes();
AddSummColumns();
ComplexCodes("55");
ComplexCodes("56");
ComplexCodes("79");
ComplexCodes("90");
ComplexCodes("93");
ComplexCodes("95");

ExSheet.Save();
ExSheet.Close(true);
Excel.Application.Quit();

WScript.Echo("Done!");