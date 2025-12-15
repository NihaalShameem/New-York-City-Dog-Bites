-- ============================================================================
-- NYC DOG BITES DATABASE - TABLE CREATION & DATA IMPORT
-- ============================================================================
-- Purpose: Create and populate dog bites incident table with NYC DOHMH data
-- Key Design: 
--   - Breed & ZipCode allow NULL (missing data in source: 9.8% and 25.8%)
--   - Age uses -1 for unknown, Gender uses 'U' (source conventions)
--   - All incidents have DateOfBite and Borough (required fields)
-- ============================================================================

IF OBJECT_ID('dbo.bites','U') IS NOT NULL   
    DROP TABLE dbo.bites;
GO 

CREATE TABLE dbo.bites (
    Unique_id INT NOT NULL, -- Original Incident ID
    DateOfBite DATE NOT NULL, -- Date incident occured
    Breed VARCHAR(100) NULL, -- Dog Breed (allows NULL for unknown)
    Age SMALLINT NOT NULL, -- Dog age in years (-1 = unknown)
    Gender NVARCHAR(50), -- Dog gender (M/F/U)
    SpayNeuter VARCHAR(50) NOT NULL, -- Spay/Neuter status (TRUE/FALSE)
    Borough VARCHAR(50) NOT NULL, -- NYC borough where incident occured
    ZipCode VARCHAR(50) NULL -- ZIP code (allows NULL for missing)
);
GO
  
-- Load data from CSV file via BULK INSERT
BULK INSERT dbo.bites
FROM 'your_file'
WITH (
    FIRSTROW = 2,                -- Skip header row
    FIELDTERMINATOR = ',',       -- Comma-delimited CSV
    ROWTERMINATOR = '\n',        -- Standard line breaks
    FORMAT = 'CSV'               -- CSV format specification
);

-- Verify successful data load
SELECT 
COUNT(*) AS total_records,
MIN(DateOfBite) AS earliest_incident,
MAX(DateOfBite) AS latest_incident,
COUNT(DISTINCT Borough) AS borough_count
FROM dbo.bites
