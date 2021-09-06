import React from "react";
import PriceTag from "./priceTag";
import Thumbnail from "./thumbnail";
import ThumbnailPlaceholder from "./thumbnailPlaceholder";
import {Link} from "react-router-dom";

class ProductDetails extends React.Component {
    render() {
        let prices_list;
        if (this.props.details.current_prices) {
                prices_list = this.props.details.current_prices.map((price) => <PriceTag key={price.slug} price={price}/>)
            }

        let price = this.props.details.price && <PriceTag price={{
                price: this.props.details.price,
                timestamp: this.props.details.timestamp,
                available: this.props.details.available,
                store: this.props.details.store,
            }} />

        let thumbnail;
        if (this.props.details.image_url) {
            thumbnail = <Thumbnail image_url={this.props.details.image_url}/>
        } else {
            thumbnail = <ThumbnailPlaceholder />
        }
        return (
            <div className={'product-details'}>
                {thumbnail}
                <Link to={this.props.details.url}><h1>{this.props.details.name}</h1></Link>
                {prices_list}
                {price}
                <p>{this.props.details.category}</p>
            </div>

        )

    }
}

export default ProductDetails