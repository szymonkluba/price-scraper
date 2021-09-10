import React from "react";
import ProductDetails from "./productDetails";
import Thumbnail from "./thumbnail";
import ThumbnailPlaceholder from "./thumbnailPlaceholder";

class ProductCard extends React.Component {
    render() {
        const details = {
            current_prices: this.props.product.current_prices,
            name: this.props.product.name,
            slug: this.props.product.slug,
            url: this.props.product.url,
            category: this.props.product.category,
            price: this.props.product.price,
            timestamp: this.props.product.timestamp,
            available: this.props.product.available,
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