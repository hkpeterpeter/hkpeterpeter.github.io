var gulp = require('gulp');
var htmlmin = require('gulp-htmlmin');

gulp.task('minify', function() {
    return gulp.src('public/**/*.html')
        .pipe(htmlmin({collapseWhitespace: true}))
        .pipe(gulp.dest('public'));
});

// For gulp v4, series and parallel are new APIs introduced
gulp.task('default', gulp.series('minify', (done) => {
    done();
}));