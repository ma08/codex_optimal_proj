/**
 * Created by huangxinghui on 2015/5/29.
 */

var $ = require('jquery')
var _ = require('underscore')
var Backbone = require('backbone')
var file = require('./file.html')
var FileModel = require('./file-model')
var FileCollection = require('./file-collection')
var FileItemView = require('./file-item-view')

var FileView = Backbone.View.extend({
  events: {
    'click .file-item': '_onClickItem'
  },

  initialize: function () {
    this.collection = new FileCollection()
    this.listenTo(this.collection, 'add', this._addFile)
    this.listenTo(this.collection, 'reset', this._addAllFiles)
    this.listenTo(this.collection, 'remove', this._removeFile)
    this.collection.fetch()
  },

  render: function () {
    this.$el.html(file())
    this.$fileList = this.$('.file-list')
    return this
  },

  _addFile: function (item) {
    var itemView = new FileItemView({
      model: item
    })
    this.$fileList.append(itemView.render().el)
  },

  _addAllFiles: function () {
    this.collection.each(this._addFile, this)
  },

  _removeFile: function (item) {
    item.destroy()
  },

  _onClickItem: function (event) {
    var $target = $(event.currentTarget)
    var id = $target.data('id')
    var model = this.collection.get(id)
    this.trigger('click:item', model)
  }
})

module.exports = FileView
/**
 * Created by huangxinghui on 2015/5/29.
 */

var $ = require('jquery')
var _ = require('underscore')
var Backbone = require('backbone')
var file = require('./file.html')
var FileModel = require('./file-model')
var FileCollection = require('./file-collection')
var FileItemView = require('./file-item-view')

var FileView = Backbone.View.extend({
  events: {
    'click .file-item': '_onClickItem'
  },

  initialize: function () {
    this.collection = new FileCollection()
    this.listenTo(this.collection, 'add', this._addFile)
    this.listenTo(this.collection, 'reset', this._addAllFiles)
    this.listenTo(this.collection, 'remove', this._removeFile)
    this.collection.fetch()
  },

  render: function () {
    this.$el.html(file())
    this.$fileList = this.$('.file-list')
    return this
  },

  _addFile: function (item) {
    var itemView = new FileItemView({
      model: item
    })
    this.$fileList.append(itemView.render().el)
  },

  _addAllFiles: function () {
    this.collection.each(this._addFile, this)
  },

  _removeFile: function (item) {
    item.destroy()
  },

  _onClickItem: function (event) {
    var $target = $(event.currentTarget)
    var id = $target.data('id')
    var model = this.collection.get(id)
    this.trigger('click:item', model)
  }
})

module.exports = FileView
