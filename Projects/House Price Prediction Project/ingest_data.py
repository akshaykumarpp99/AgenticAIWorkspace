from abc import ABC, abstractmethod
import os
import pandas as pd
import zipfile

class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        """Abstarct method used to ingest data from a given file"""
        pass
    
class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path: str) -> pd.DataFrame:
        if not file_path.endswith(".zip"):
            raise ValueError("The existing file is not a zip file")
        
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall("extracted_data")
        
        extracted_files = os.listdir("extracted_data")
        csv_files = [f for f in extracted_files if f.endswith(".csv")]
        print(csv_files)
        
        if len(csv_files) == 0:
            raise ValueError("No CSV file found in the zip file")
        if len(csv_files) > 1:
            raise ValueError("Multiple CSV files found in the zip file")
        
        csv_file_path = os.path.join("extracted_data", csv_files[0])
        df = pd.read_csv(csv_file_path)
        print(df.head(10))
        
zipIngest = ZipDataIngestor()
zipIngest.ingest("New Business.zip")