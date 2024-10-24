var FSO = new ActiveXObject("Scripting.FileSystemObject");
var Excel = new ActiveXObject("Excel.Application");
var ExSheet;

var Codes = new Array(
"33.11",
"45.20",
"49.1",
"49.10",
"49.3",
"49.31",
"49.32",
"49.39",
"53.20.29",
"53.20.3",
"53.20.31",
"53.20.32",
"53.20.39",
"55.1",
"55.2",
"56.1",
"56.10",
"79.1",
"79.11",
"79.12",
"79.9",
"79.90",
"79.90.1",
"79.90.2",
"79.90.21",
"79.90.22",
"79.90.3",
"79.90.31",
"79.90.32",
"81.1",
"81.2",
"81.21",
"81.21.1",
"81.22",
"85.42.1",
"85.42.9",
"86.90.3",
"86.90.4",
"86.90.9",
"93.11",
"93.12",
"93.13",
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
"95.29.13",
"95.29.2",
"95.29.3",
"95.29.4",
"95.29.41",
"95.29.42",
"95.29.43",
"95.29.5",
"95.29.6",
"95.29.7",
"95.29.9",
"96.0",
"96.01",
"96.02",
"96.02.1",
"96.02.2",
"96.03",
"96.04",
"96.09",
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

var FileName = new Array();
function GetFileName()
{
	ind = 0;
	//FileName = "";
	Folder = FSO.GetFolder(GetPath());
	fc = new Enumerator(Folder.files);
	for(; !fc.atEnd(); fc.moveNext())
	{
		if (fc.item().Name.substr(0, 11) == "ŒÚ˜ÂÚ Œ ¬›ƒ")
		{
			FileName[ind] =  fc.item().Name;
			ind++;
		}
	}
	return FileName[0];
}

function NewFileName(OrginalName)
{
	NewName = OrginalName.substr(0, 5) + "3" + OrginalName.substr(5, OrginalName.length - 5);
	return NewName;
}

// =======   Main   =======
GetFileName();


for(s=0; s<FileName.length; s++)
{
	FSO.CopyFile(FileName[s], NewFileName(FileName[s]));
	ExSheet = Excel.Workbooks.Open(GetPath()+"\\"+NewFileName(FileName[s]));
	ExSheet.Application.Visible = false;

	DeleteSheets();
	DeleteCodes();
	AddSummColumns();

	//ComplexCodes("55");
	//ComplexCodes("56");
	//ComplexCodes("79");
	//ComplexCodes("90");
	//ComplexCodes("93");
	//ComplexCodes("95");

	ExSheet.Save();
	ExSheet.Close(true);
	Excel.Application.Quit();
}

WScript.Echo("Done!");