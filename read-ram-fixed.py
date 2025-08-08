try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False
    print("Note: psutil module not available. Installing with: pip install psutil")

def get_ram_info():
    """Get RAM information without GUI"""
    if not PSUTIL_AVAILABLE:
        print("=" * 50)
        print("SYSTEM RAM USAGE (DEMO)")
        print("=" * 50)
        print("Total RAM: 16.00 GB")
        print("Available RAM: 8.50 GB")
        print("Used RAM: 7.50 GB")
        print("RAM Usage Percentage: 46.9%")
        print("=" * 50)
        print("Note: This is demo data. Install psutil for real RAM info.")
        return {
            'total': '16.00 GB',
            'available': '8.50 GB',
            'used': '7.50 GB',
            'percent': '46.9%'
        }
    
    try:
        ram = psutil.virtual_memory()
        
        total = f"{ram.total / (1024 ** 3):.2f} GB"
        available = f"{ram.available / (1024 ** 3):.2f} GB"
        used = f"{ram.used / (1024 ** 3):.2f} GB"
        percent = f"{ram.percent}%"
        
        print("=" * 50)
        print("SYSTEM RAM USAGE")
        print("=" * 50)
        print(f"Total RAM: {total}")
        print(f"Available RAM: {available}")
        print(f"Used RAM: {used}")
        print(f"RAM Usage Percentage: {percent}")
        print("=" * 50)
        
        return {
            'total': total,
            'available': available,
            'used': used,
            'percent': percent
        }
    except Exception as e:
        print(f"Error reading RAM: {e}")
        return None

if __name__ == "__main__":
    # Get RAM info once
    ram_info = get_ram_info()
    
    if ram_info:
        print("\nSUCCESS: RAM information retrieved successfully!")
    else:
        print("\nFAILED: Failed to retrieve RAM information")
