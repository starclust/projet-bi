import { Component } from '@angular/core';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';


@Component({
  selector: 'app-purchasing-manager',
  templateUrl: './purchasing-manager.component.html',
  styleUrls: ['./purchasing-manager.component.css']
})
export class PurchasingManagerComponent {
  showPowerBI: boolean = true;
  showPrediction: boolean = false;
 
  powerBIUrl: SafeResourceUrl;
  predictionUrl: SafeResourceUrl;

  constructor(private sanitizer: DomSanitizer) {
    // Mets ici ton URL Power BI officielle
    this.powerBIUrl = this.sanitizer.bypassSecurityTrustResourceUrl(
      'https://app.powerbi.com/reportEmbed?reportId=c5c36603-28c3-47b9-aee0-e0954d41baa4&autoAuth=true&ctid=604f1a96-cbe8-43f8-abbf-f8eaf5d85730'
    );

    // Mets ici l'URL de ton serveur Flask déployé
    this.predictionUrl = this.sanitizer.bypassSecurityTrustResourceUrl(
      'http://127.0.0.1:5000'
    );
  }

  showPowerBIView(): void {
    this.showPowerBI = true;
    this.showPrediction = false;
  }

  showPredictionView(): void {
    this.showPowerBI = false;
    this.showPrediction = true;
  }
}
