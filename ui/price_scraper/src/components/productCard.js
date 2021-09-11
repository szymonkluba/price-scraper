import React from "react";
import ProductDetails from "./productDetails";
import Thumbnail from "./thumbnail";
import ThumbnailPlaceholder from "./thumbnailPlaceholder";

class ProductCard extends React.Component {
    render() {
        const details = {
            ...this.props.product
        }
        let thumbnail;
        if (this.props.product.image_url) {
            thumbnail = <Thumbnail image_url={this.props.product.image_url}/>
        } else {
            thumbnail = <ThumbnailPlaceholder />
        }
        return (
            <div className={'product-card'}>
                {thumbnail}
                <ProductDetails details={details} />
            </div>
        );
    }
}

export default ProductCard