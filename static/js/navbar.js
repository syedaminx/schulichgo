window.onload = function() {

  // hamburger menu when on mobile
  $(document).ready(function() {
    $('.hamburger').click(function(e) {
      $menu = $(this).parent();
      if (!$(this).hasClass('active')) {
        $(this).addClass('active');
        $menu.addClass('open');
      } else {
        $(this).removeClass('active');
        $menu.removeClass('open');
      }
      e.preventDefault();
    });
  })

  // hardcoded search values for development
  var categoryContent = [
    {
      category: 'ACTG 2010',
      title: 'Introduction To Financial Accounting I'
    }, {
      category: 'ACTG 2020',
      title: 'Intermediate Financial Accounting I'
    }, {
      category: 'MKTG 2030',
      title: 'Marketing'
    }, {
      category: 'EMBA 6320',
      title: 'Value Investing'
    }, {
      category: 'Asia',
      title: 'Japan'
    }, {
      category: 'Asia',
      title: 'China'
    }, {
      category: 'Europe',
      title: 'Denmark'
    }, {
      category: 'Europe',
      title: 'England'
    }, {
      category: 'Europe',
      title: 'France'
    }, {
      category: 'Europe',
      title: 'Germany'
    }, {
      category: 'Africa',
      title: 'Ethiopia'
    }, {
      category: 'Africa',
      title: 'Nigeria'
    }, {
      category: 'Africa',
      title: 'Zimbabwe'
    }
  ];

  // search script
  $('.ui.search').search({type: 'category', source: categoryContent});
}
