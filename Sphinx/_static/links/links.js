/* -*- coding: latin-1 -*- */

function img_load(item, url) {
    /*
      If item first child is <img src="#"> tag
      then set this to <img src="url">
           and if item second child is <* class="size"> tag
               then set this to <_ class="size">size of image</_>.

      Pre: item: DOM item
           url: String
    */
    'use strict';

    var children = item.children;

    if ( (children.length > 0) && (children[0].tagName === 'IMG') ) {
        if ( children[0].getAttribute('src') === '#' ) {
            children[0].setAttribute('src', url);
        }

        if ( (children.length > 1) && (children[1].className === 'size') && (children[1].children.length > 0) ) {
            children[1].children[0].innerHTML = children[0].width.toString() + 'x' + children[0].height.toString();
        }
    }
}
