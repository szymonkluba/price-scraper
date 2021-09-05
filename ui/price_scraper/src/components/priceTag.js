import React from "react";
import moment from "moment";

class PriceTag extends React.Component {
    render() {
        return (
            <div>
                <span>{this.props.price.store}</span>
                <span>{this.props.price.price}</span>
                <span className={this.props.price.available ? 'available' : 'unavailable'}>{this.props.price.available ? 'yes' : 'no'}</span>
                <span>{moment(this.props.price.timestamp, moment.ISO_8601).fromNow()}</span>
            </div>
        );
    }
}

export default PriceTag