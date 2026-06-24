from src.app.models.vehicle.vehicle import Vehicle
from src.app.models.vehicle.vehicleSpecs import VehicleSpecs
from src.app.models.vehicle.vehiclePricing import VehiclePricing
from src.app.models.vehicle.vehicleDocuments import VehicleDocuments
from src.app.models.vehicle.vehicleHistory import VehicleHistory
from src.app.models.vehicle.vehicleMedia import VehicleMedia
from src.app.schemas.vehicle.vehicle import VehicleRequest, VehicleResponse

class VehicleMapper:

    @staticmethod
    def to_model(data: VehicleRequest) -> Vehicle:
        vehicle = Vehicle(
            vehicle_type=data.vehicle_type,
            title=data.title,
            description=data.description,
            make=data.make,
            model=data.model,
            trim=data.trim,
            year_of_manufacture=data.year_of_manufacture,
            condition=data.condition,
            status=data.status,
            district=data.district,
            city=data.city,
            is_featured=data.is_featured,
            is_verified=data.is_verified,
        )

        # Build related ORM objects; vehicle_id is set automatically on flush.
        if data.specs is not None:
            vehicle.specs = VehicleSpecs(**data.specs.model_dump())

        if data.pricing is not None:
            vehicle.pricing = VehiclePricing(**data.pricing.model_dump())

        if data.documents is not None:
            vehicle.documents = VehicleDocuments(**data.documents.model_dump())

        if data.history is not None:
            vehicle.history = VehicleHistory(**data.history.model_dump())

        if data.media:
            vehicle.media = [VehicleMedia(**item.model_dump()) for item in data.media]

        return vehicle

    @staticmethod
    def to_response(model: Vehicle) -> VehicleResponse:
        return VehicleResponse.model_validate(model)
