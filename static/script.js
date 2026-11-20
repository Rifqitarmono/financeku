// Fungsi untuk membuka / menutup sidebar pada layar mobile & tablet
function toggleSidebar() {
    var sidebar = document.getElementById('appSidebar');
    var overlay = document.getElementById('sidebarOverlay');

    if (sidebar) {
        sidebar.classList.toggle('open');
    }
    if (overlay) {
        overlay.classList.toggle('active');
    }
}

// Fungsi interaktif untuk memilih menu sidebar aktif
function pilihMenu(elemenYangDiklik) {
    // Ambil semua item menu di sidebar
    var semuaMenu = document.querySelectorAll('.menu-item');

    // Hapus class 'active' dari semua menu
    for (var i = 0; i < semuaMenu.length; i++) {
        semuaMenu[i].classList.remove('active');
    }

    // Tambahkan class 'active' ke menu yang baru diklik
    elemenYangDiklik.classList.add('active');

    // Jika sedang di layar mobile/tablet (lebar <= 860px), tutup sidebar secara otomatis setelah menu diklik
    if (window.innerWidth <= 860) {
        var sidebar = document.getElementById('appSidebar');
        var overlay = document.getElementById('sidebarOverlay');
        if (sidebar && sidebar.classList.contains('open')) {
            sidebar.classList.remove('open');
        }
        if (overlay && overlay.classList.contains('active')) {
            overlay.classList.remove('active');
        }
    }
}
