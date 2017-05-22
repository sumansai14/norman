const path = require('path');
const webpack = require('webpack');
const autoprefixer = require('autoprefixer');
const ExtractTextPlugin = require("extract-text-webpack-plugin");

var staticPrefix = 'norman/static/norman',
    distPath = staticPrefix + '/dist';

const config = {
    entry: {
        build: [
            'webpack-dev-server/client?http://0.0.0.0:8080', // WebpackDevServer host and port
            'webpack/hot/only-dev-server',
            path.resolve(path.join(staticPrefix, 'scss', 'norman.scss'))
        ],
        vendor: ['bootstrap']
    },
    module: {
        rules: [{
            test: /\.scss$/,
            exclude: /(node_modules|bower_components)/,
            use: ExtractTextPlugin.extract({
                use: [
                    'css-loader',
                    {
                        loader: 'postcss-loader',
                        options: {
                            plugins: [autoprefixer({browsers: ['> 1%', 'last 2 versions']})]
                        }
                    },
                    {
                        loader: 'sass-loader',
                        options: {
                            includePaths: [path.join(staticPrefix, 'scss')]
                        }
                    }
                ]
            })
        }]
                // {test: /\.(png|woff|woff2|eot|ttf|svg)$/, loader: 'url-loader?limit=100000'}]
    },
    externals: {
        // don't bundle the jquery npm package with our bundle.js
        // but get it from a global jQuery variable
        jquery: 'jQuery',
        tether: 'Tether'
    },
    output: {
        path: path.join(__dirname, distPath),
        filename: '[name].js',
        sourceMapFilename: '[name].js.map',
        publicPath: '/assets/'
    },
    plugins: [
        new ExtractTextPlugin('norman.css'),
        new webpack.ProvidePlugin({
            "$": "jquery",
            jQuery: "jquery",
            "window.jQuery": "jquery",
            "window.Tether": 'tether'
        })
    ],
    target: 'web',
    resolveLoader: {
        moduleExtensions: ['-loader']
    }
};

module.exports = config;